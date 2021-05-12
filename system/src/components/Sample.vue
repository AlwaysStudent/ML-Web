<template>
  <div class="sample-box">
    <div class="picture-group">
      <div class="picture-mix-matrix">
        <el-image
            fit="contain" :src="beforePictureSrc" :preview-src-list="srcList">
          <div slot="error" class="image-slot"></div>
        </el-image>
      </div>
      <div class="picture-accuracy">
        <el-image
            fit="contain" :src="afterPictureSrc" :preview-src-list="srcList">
          <div slot="error" class="image-slot"></div>
        </el-image>
      </div>
    </div>
    <div class="button">
      <div class="mix-matrix-button">
        <el-button @click="loadingBeforePicture">
          加载原始数据比
        </el-button>
      </div>
      <div class="accuracy-button">
        <el-button @click="loadingAfterPicture">
          数据采样
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import bus from '../bus/bus'

export default {
  name: "Sample",
  mounted() {
    bus.$on('selectedDataset', (dataset) => {
      this.dataset = dataset
      this.reset()
    })
  },
  data(){
    return {
      dataset: '',
      beforePictureSrc: '',
      afterPictureSrc: '',
      srcList: [],
    }
  },
  methods: {
    reset() {
      this.beforePictureSrc = ''
      this.afterPictureSrc = ''
      this.srcList = []
    },
    async loadingBeforePicture() {
      let config = {
        headers: {
          'Content-Type': 'image/png',
        }
      }
      let res1 = axios.post(
          'http://127.0.0.1:8888/handle/sample',
          {
            'data': this.dataset,
            'now': 'before'
          },
          config
      )
      res1.then(value => {
        this.beforePictureSrc = "data:image/png;base64," + value.data
        this.srcList.push("data:image/png;base64," + value.data)
      })
    },
    async loadingAfterPicture() {
      let config = {
        headers: {
          'Content-Type': 'image/png',
        }
      }
      let res2 = axios.post(
          'http://127.0.0.1:8888/handle/sample',
          {
            'data': this.dataset,
            'now': 'after'
          },
          config
      )
      res2.then(value => {
        this.afterPictureSrc = "data:image/png;base64," + value.data
        this.srcList.push("data:image/png;base64," + value.data)
      })
    },
  }
}
</script>

<style scoped>
.sample-box {
  width: 90vw;
  height: 85vh;
}
.picture-group {
  margin-top: 5vh;
  width: 100%;
  height: 80%;
  display: flex;
  justify-content: center;
}
.picture-mix-matrix {
  margin-right: 4%;
  width: 40%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.picture-accuracy {
  margin-left: 4%;
  width: 40%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.button {
  margin-top: 4vh;
  display: flex;
  justify-content: center;
}
.mix-matrix-button {
  margin-right: 20px;
}
.accuracy-button {
  margin-left: 20px;
}
</style>