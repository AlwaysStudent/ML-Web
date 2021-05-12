<template>
  <div class="special-select">
    <div class="table-picture">
      <div class="picture">
        <el-image fit="contain" :src="pictureSrc" :preview-src-list="srcList">
          <div slot="error" class="image-slot"></div>
        </el-image>
      </div>
      <div class="table">
        <el-table
            :data="tableData"
            stripe
            height="100%"
            v-loading="tableLoading"
            element-loading-text="拼命加载中"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(0, 0, 0, 0.8)"
            :empty-text="emptyText">
          <template v-for="(item, index) in tableLabel">
            <el-table-column :prop="item['prop']" :label="item['label']" :key="index"></el-table-column>
          </template>
        </el-table>
      </div>
    </div>
    <div class="loading-button">
      <div class="picture-loading-button">
        <el-button @click="loadingPicture">
          加载热力图
        </el-button>
      </div>
      <div class="data-loading-button">
        <el-button @click="loadingData">
          加载数据
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import bus from "../bus/bus"
import axios from "axios";

export default {
  name: "Select",
  mounted() {
    bus.$on('selectedDataset', (dataset) => {
      this.dataset = dataset
      this.reset()
    })
  },
  data() {
    return {
      dataset: '',
      pictureSrc: '',
      srcList: [],
      tableLabel: [],
      tableData: [],
      tableLoading: false,
      emptyText: '等待加载'
    }
  },
  methods: {
    reset() {
      this.pictureSrc = ''
      this.srcList = []
      this.tableLabel = []
      this.tableData = []
      this.tableLoading = false
      this.emptyText = '等待加载'
    },
    async loadingData() {
      this.tableLoading = true
      this.emptyText = '  '
      this.tableLabel = []
      this.tableData = []
      console.log(this.dataset)
      let res = await axios.post(
          'http://127.0.0.1:8888/handle/select',
          {
            'data': this.dataset,
          }
      )
      console.log(res)
      this.tableLabel = res.data.tableLabel
      for (let i = 0;i < res.data.tableData.length;i++) {
        this.tableData.push(JSON.parse(res.data.tableData[i]))
      }
      this.tableLoading = false
    },
    async loadingPicture() {
      this.pictureLoading = true
      let config = {
        headers: {
          'Content-Type': 'image/png',
        }
      }
      let res = axios.post(
          'http://127.0.0.1:8888/handle/select-picture',
          {
            'data': this.dataset,
          },
          config
      )
      res.then(value => {
        this.pictureSrc = "data:image/png;base64," + value.data
        this.srcList = []
        this.srcList.push("data:image/png;base64," + value.data)
      })
      this.pictureLoading = false
    }
  }
}
</script>

<style scoped>
.special-select {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  align-items: center;
  justify-items: center;
}
.table-picture {
  margin-top: 10vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-items: center;
  width: 100%;
  height: 60vh;
}
.table {
  width: 50%;
  margin-left: 4%;
  height: 100%;
}
.picture {
  border: #62676c 1px solid;
  margin-left: 4%;
  width: 40%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.loading-button {
  margin-top: 7%;
  display: flex;
  align-items: center;
}
.picture-loading-button {
  margin-right: 5vw;
}
.data-loading-button {
  margin-right: 5vw;
}
</style>