<template>
  <div class="model_predict">
    <div class="picture-group">
      <div class="">
        <el-image fit="contain" src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" :preview-src-list="srcList">
          <div slot="error" class="image-slot">
            <i class="el-icon-picture-outline"></i>
          </div>
        </el-image>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Model",
  data() {
    return {
      srcList: [
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
      ]
    }
  }
}
</script>

<style scoped>

</style>