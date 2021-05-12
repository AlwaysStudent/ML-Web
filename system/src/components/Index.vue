<template>
  <div class="index">
    <div class="index-content">
      <div class="introduce">
        <img src="@/assets/title.png" alt="">
      </div>
      <div class="button-box">
        <el-button type="primary" @click="enterClick('/handle')" round>进入</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import bus from '../bus/bus'

export default {
  name: "Index",
  methods: {
    enterClick(index) {
      bus.$emit('enterClick', index)
      this.$router.push(index)
    }
  },
}
</script>

<style scoped>
.index-content {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  justify-items: center;
  align-items: center;
}
.introduce {
  margin-top: 30vh;
}
.button-box {
  margin-top: 20vh;
}
/deep/ .el-button {
  width: 160px;
  height: 60px;
  font-size: 20px;
}
</style>