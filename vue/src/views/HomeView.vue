<template>
    <div class="flex flex-col mx-40 my-1.5" >
        <div style="text-align: -webkit-center;">
        <Form>
            <TextArea id="textarea-input" label="Tweet" v-model="content" row="5" />
            <div class="flex flex-row space-x-3">
                <Button type="submit" name="Submit"
                    @click="handleSubmit" />
                <Button type="button" name="Upload Image" @click="toggleModal" />
            </div>
        </Form>
        </div>
        <section>
            <p class="text-2xl font-semibold mt-4">Other Tweets</p>
            <Card v-for="item in tweets.items.data" :key="item.user_id" :user="item.user.username" :tweet="item.content"
                :imgPath="item.image_path" :imgName="item.image_name" @buttonClicked="getPostId()" />
            <!-- pagination -->
            <div class="pagination flex justify-center gap-10 items-center">
                <button @click="prevPage" :disabled="page === 1"
                    class="bg-green-500 p-2 mt-3 rounded-md text-white hover:bg-green-800 disabled:bg-gray-500">Previous</button>
                <span class="text-xl">{{ page }} of {{ tweets.total_pages }}</span>
                <button @click="nextPage" :disabled="page === tweets.total_pages"
                    class="bg-green-500 p-2 mt-3 rounded-md text-white hover:bg-green-800 disabled:bg-gray-500">Next</button>
            </div>

        </section>

        <!-- section overlay -->
        <Teleport to="body">
            <ModalUpload @toggle-modal="toggleModal" :show-modal="showModal">
                <Form>
                    <label for="uploadBtn">Upload</label>
                    <label for="uploadFile" class="flex  justify-center p-5 rounded-md">
                        <InputFile button-text="Upload" id="uploadBtn" v-model="formData.file" />
                    </label>
                    <TextArea id="textarea-input" label="Tweet" v-model="formData.content" row="5" />
                    <div class="flex flex-row space-x-3">
                        <Button type="submit" name="Submit" @click="handleUploadFile" />
                        <Button type="button" name="Close" @click="toggleModal" />
                    </div>
                </Form>
            </ModalUpload>
        </Teleport>
    </div>
    <Teleport to="body">
        <ModalNotifikasi @toggle-modal="toggleModal" :show-modal="showModalNotif" modal-title="Notifikasi"
            :modal-desc="msg">
            <Button type="button" name="Close" @click="toggleModalNotif" />
        </ModalNotifikasi>
    </Teleport>
</template>
  
<script setup>
import Card from '../components/ui/card.vue';
import Form from '../components/ui/form.vue';
import TextArea from '../components/ui/textArea.vue'
import Button from '../components/ui/button.vue';
import { ref, onMounted, reactive, watch } from 'vue'
import ModalUpload from '../components/ui/modalUpload.vue';
import InputFile from '../components/ui/inputFile.vue';
import { useFetch } from '../composable/useFetch';
import ModalNotifikasi from '../components/ui/modalNotification.vue'

const { tryFetching, tryPosting, success, tryUpload } = useFetch()

const formData = reactive({
    content: '',
    file: ''
})
const content = ref('')
const tweetId = ref(null)
const userId = ref(null)
// const content = ref('')
// const uploadedFile = ref(null)
const page = ref(1)
const tweets = reactive({
    items: [],
    per_page: 10,
    total_pages: 1,
    total_items: 0,
})



onMounted(async () => {
    const res = await tryFetching('/api/tweets', page.value, tweets.per_page)
    tweets.items = res.data
    page.value = res.data.page
    tweets.total_items = res.data.total_item
    tweets.total_pages = res.data.total_page
})


const prevPage = () => {
    page.value--
};
const nextPage = () => {
    page.value++
};


const tryFetchData = async () => {
    try {
        const res = await tryFetching('/api/tweets', page.value, tweets.per_page)
        console.log(res.data)
        tweets.items = res.data
        page.value = res.data.page
        tweets.total_items = res.data.total_item
        tweets.total_pages = res.data.total_page
    } catch (e) {
        console.log(e)
    }
}

watch(page, () => {
    tryFetchData()
})



const showModalNotif = ref(false)
const showModal = ref(false)
const msg = ref('')
const toggleModal = () => {
    showModal.value = !showModal.value
}
const toggleModalNotif = () => {
    showModalNotif.value = !showModalNotif.value
}

const handleSubmit = async () => {
    await tryPosting("/api/tweets", { "content": content.value })
    if (success.value = true) {
        showModalNotif.value = true
        msg.value = "Berhasil Menambahkan tweet!"
    }
}

const handleUploadFile = async () => {
    await tryUpload("/api/tweets", formData)
    if (success.value == true) {
        toggleModal()
    }

}

</script>
  
