<template>
  <div class="navbar">
    <div class="logo">
      <div>
        <img src="@/assets/logo.png" alt="" style="height: 60px;">
      </div>
    </div>
    <el-menu
        ref="nav"
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#f3b6b6"
        text-color="#606266"
        active-text-color="#FFFFFF"
        router>
      <el-menu-item index="/" class="tab">首页</el-menu-item>
      <el-menu-item index="/handle" class="tab">数据处理展示</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import bus from '../bus/bus'

export default {
  name: "Nav",
  data() {
    return {
      activeIndex: ''
    }
  },
  created() {
    this.activeIndex = this.$route.path
  },
  mounted() {
    bus.$on('enterClick', (index) => {
      this.activeIndex = index
      this.$refs.nav.$data.activeIndex = index
    })
  }
}
</script>

<style scoped>
.navbar {
  height: 60px;
  display: flex;
  justify-content: space-between;
  background-color: #f3b6b6;
  border-bottom: solid 1px #e6e6e6;
}
</style>