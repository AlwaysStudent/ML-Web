<template>
  <div class="special-select">
    <div class="table-picture">
      <div class="picture">
        <el-image fit="contain" :src="pictureSrc" :preview-src-list="srcList">
          <div slot="error" class="image-slot">
            <i class="el-icon-picture-outline"></i>
          </div>
        </el-image>
      </div>
      <div class="table">
        <el-table :data="tableData" stripe height="100%">
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
    })
  },
  data() {
    return {
      dataset: '',
      pictureSrc: '',
      srcList: [],
      tableLabel: [],
      tableData: []
    }
  },
  methods: {
    async loadingData() {
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
    },
    async loadingPicture() {
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