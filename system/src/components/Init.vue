<template>
  <div class="init">
    <div class="select-dataset">
      <div class="select-dataset-selector">
        <el-select v-model="value" clearable placeholder="请选择" :disabled="isDatasetSelected">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </div>
      <div class="select-dataset-button">
        <el-button @click="setDataset">确定</el-button>
      </div>
      <div class="reset-dataset-button">
        <el-button @click="resetDataset">重置</el-button>
      </div>
    </div>
    <div class="choice-dataset-button">
      <el-switch v-model="choiceValue" active-text="训练集" inactive-text="测试集" @change="changeChoice">
      </el-switch>
    </div>
    <div class="showing-table">
      <el-table :data="tableData" stripe height="100%">
        <template v-for="(item, index) in tableLabel">
          <el-table-column :prop="item['prop']" :label="item['label']" :key="index"></el-table-column>
        </template>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import bus from "../bus/bus"

export default {
  name: "Init",
  data() {
    return {
      dataSet: '',
      tableLabel: [],
      isDatasetSelected: false,
      options: [
        {
          value: 'NSL_KDD',
          label: 'NSL_KDD'
        }, {
          value: 'UNSW_NB15',
          label: 'UNSW_NB15'
        }
      ],
      value: '',
      tableData: [],
      choiceValue: false
    }
  },
  methods: {
    async setDataset() {
      this.dataSet = this.value
      this.isDatasetSelected = true
      bus.$emit('selectedDataset', this.dataSet)
      let dataset = ''
      if (this.choiceValue === false) {
        dataset = 'Train'
      }
      else {
        dataset = 'Test'
      }
      let res = await axios.post(
          'http://127.0.0.1:8888/handle/init',
          {
            'data': this.value,
            'dataset': dataset
          }
      )
      console.log(res)
      this.tableLabel = res.data.tableLabel
      for (let i = 0;i < res.data.tableData.length;i++) {
        this.tableData.push(JSON.parse(res.data.tableData[i]))
      }
    },
    resetDataset() {
      this.dataSet = ''
      this.isDatasetSelected = false
      this.tableLabel = []
      this.tableData = []
    },
    async changeChoice() {
      this.tableLabel = []
      this.tableData = []
      let dataset = ''
      if (this.choiceValue === false) {
        dataset = 'Train'
      }
      else {
        dataset = 'Test'
      }
      let res = await axios.post(
          'http://127.0.0.1:8888/handle/init',
          {
            'data': this.value,
            'dataset': dataset
          }
      )
      console.log(res)
      this.tableLabel = res.data.tableLabel
      for (let i = 0;i < res.data.tableData.length;i++) {
        this.tableData.push(JSON.parse(res.data.tableData[i]))
      }
    }
  }
}
</script>

<style scoped>
.init{
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  align-items: center;
}
.select-dataset {
  margin-top: 8vh;
  display: flex;
  justify-content: center;
  opacity: 0.8;
}
.select-dataset-selector {
  margin-right: 6vw;
}
.reset-dataset-button {
  margin-left: 6vw;
}
.choice-dataset-button {
  margin-top: 5vh;
}
.showing-table {
  align-self: flex-start;
  margin-top: 5vh;
  width: 99%;
  opacity: 0.8;
  height: 60vh;
}
</style>