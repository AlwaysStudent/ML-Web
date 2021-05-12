<template>
  <div class="pre-handle">
    <div class="datasetIntroduce">
      <div>选择的数据集: {{this.dataset}}</div>
      <div>Introduce</div>
      <div class="loading-button">
        <el-button @click="loadingData">
          加载预处理的测试集数据
        </el-button>
      </div>
    </div>
    <div class="showing-table">
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
</template>

<script>
import bus from "../bus/bus";
import axios from "axios";

export default {
  name: "PreHandle",
  data() {
    return {
      dataset: '',
      tableLabel: [],
      tableData: [],
      tableLoading: false,
      emptyText: '等待加载'
    }
  },
  mounted() {
    bus.$on('selectedDataset', (dataset) => {
      this.dataset = dataset
      this.reset()
    })
  },
  methods: {
    reset(){
      this.tableLabel = []
      this.tableData = []
      this.tableLoading = false
      this.emptyText = '等待加载'
    },
    async loadingData() {
      this.emptyText = '  '
      this.tableLoading = true
      this.tableLabel = []
      this.tableData = []
      console.log(this.dataset)
      let res = await axios.post(
          'http://127.0.0.1:8888/handle/pre',
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
    }
  }
}
</script>

<style scoped>
.pre-handle {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  align-items: flex-start;
}
.datasetIntroduce {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  align-items: flex-start;
}
.datasetIntroduce > div {
  margin-top: 3vh;
  margin-left: 3vw;
}
.showing-table {
  align-self: flex-start;
  margin-top: 5vh;
  width: 99%;
  opacity: 0.8;
  height: 60vh;
}
.loading-button {
  align-self: flex-end;
}
</style>