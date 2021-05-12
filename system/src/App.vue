<template>
  <div id="app">
    <Nav></Nav>
    <router-view></router-view>
  </div>
</template>

<script>
import Nav from './components/Nav'

export default {
  name: 'App',
  components: {
    Nav,
  },
}
</script>

<style>
#app {
  margin: 0;
  padding: 0;
  height: 100vh;
}
html {
  margin: 0;
  padding: 0;
  height: 100vh;
}
body {
  margin: 0;
  padding: 0;
  height: 100vh;
  background: linear-gradient(#f3b6b6, #abd0f6);
}
</style>
