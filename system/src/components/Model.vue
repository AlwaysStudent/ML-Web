<template>
  <div class="model-box">
    <div class="picture-group">
      <div class="picture-mix-matrix">
        <el-image
            fit="contain" :src="mixMatrixPictureSrc" :preview-src-list="srcList">
          <div slot="error" class="image-slot"></div>
        </el-image>
      </div>
      <div class="picture-accuracy">
        <el-image
            fit="contain" :src="accuracyPictureSrc" :preview-src-list="srcList">
          <div slot="error" class="image-slot"></div>
        </el-image>
      </div>
    </div>
    <div class="button">
      <div class="mix-matrix-button">
        <el-button @click="loadingMixMatrixPicture">
          加载混淆矩阵
        </el-button>
      </div>
      <div class="accuracy-button">
        <el-button @click="loadingAccuracyPicture">
          准确率
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import bus from "../bus/bus"
import axios from "axios";

export default {
  name: "Model",
  mounted() {
    bus.$on('selectedDataset', (dataset) => {
      this.dataset = dataset
      this.reset()
    })
  },
  data() {
    return {
      dataset: '',
      mixMatrixPictureSrc: '',
      accuracyPictureSrc: '',
      srcList: []
    }
  },
  methods: {
    reset() {
      this.mixMatrixPictureSrc = ''
      this.accuracyPictureSrc = ''
      this.srcList = []
    },
    async loadingMixMatrixPicture() {
      let config = {
        headers: {
          'Content-Type': 'image/png',
        }
      }
      let res1 = axios.post(
          'http://127.0.0.1:8888/handle/model',
          {
            'data': this.dataset,
            'picture': 'MixMatrix'
          },
          config
      )
      res1.then(value => {
        this.mixMatrixPictureSrc = "data:image/png;base64," + value.data
        this.srcList.push("data:image/png;base64," + value.data)
      })
    },
    async loadingAccuracyPicture() {
      let config = {
        headers: {
          'Content-Type': 'image/png',
        }
      }
      let res2 = axios.post(
          'http://127.0.0.1:8888/handle/model',
          {
            'data': this.dataset,
            'picture': 'Accuracy'
          },
          config
      )
      res2.then(value => {
        this.accuracyPictureSrc = "data:image/png;base64," + value.data
        this.srcList.push("data:image/png;base64," + value.data)
      })
    },
  }
}
</script>

<style scoped>
.model-box {
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