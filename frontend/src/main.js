import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { BootstrapVueIcons } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";

Vue.config.productionTip = false;
//fix bugs with multiple instance
const BootstrapVue = require("bootstrap-vue");
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
