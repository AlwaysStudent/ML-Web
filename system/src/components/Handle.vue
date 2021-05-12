<template>
  <div class="handle-box">
    <el-tabs class="tabs" tab-position="left" :value="tabSelectValue">
      <el-tab-pane name="1">
        <span slot="label">
          <i class="el-icon-thumb"></i> 数据导入
        </span>
        <Init></Init>
      </el-tab-pane>
      <el-tab-pane name="2">
        <span slot="label">
          <i class="el-icon-edit"></i> 数据预处理
        </span>
        <PreHandle></PreHandle>
      </el-tab-pane>
      <el-tab-pane name="3">
        <span slot="label">
          <i class="el-icon-finished"></i> 特征选择
        </span>
        <Select></Select>
      </el-tab-pane>
      <el-tab-pane name="4">
        <span slot="label">
          <i class="el-icon-loading"></i> 训练模型并预测
        </span>
        <Model></Model>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import Init from "./Init"
import PreHandle from "./PreHandle"
import Select from "./Select"
import Model from "./Model"

export default {
  name: "Handle",
  components: {
    Init,
    PreHandle,
    Select,
    Model
  },
  data() {
    return {
      tabSelectValue: '1',
    }
  },
  methods: {

  }
}
</script>

<style scoped>
.tabs {
  height: 90vh;
}

</style>