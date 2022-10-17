<template>
  <div class="jumbotron">
    <h1>{{ msg }}</h1>
    <p>
      一个简单的elasticsearch-flask demo程序,<br />
      更多请查看
      <a href="https://haoo.tech" target="_blank" rel="noopener">hao's page</a>
    </p>
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <!-- Alert after add teacher -->
          <b-alert variant="success" v-if="showMessage" show
            >{{ message }}
          </b-alert>
          <b-input-group style="float: left; width: 50%">
            <b-input-group-prepend is-text>
              <b-icon icon="search"></b-icon>
            </b-input-group-prepend>
            <b-form-input placeholder="请输入查询关键字" v-model="search_data">
            </b-form-input>
            <b-form-select
              v-model="selected"
              :options="options"
            ></b-form-select>
          </b-input-group>
          <b-button
            type="button"
            variant="outline-dark"
            style="float: left; margin-left: 10px"
            v-on:click="this.onSearch"
          >
            <b-icon icon="hand-index-thumb"></b-icon>
            查询
          </b-button>
          <b-button
            type="button"
            variant="outline-info"
            style="float: left; margin-left: 5px"
            v-b-modal.elastic-modal
          >
            <b-icon icon="plus-lg"></b-icon>
            添加
          </b-button>
          <br />
          <br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">序号</th>
                <th scope="col">ID</th>
                <th scope="col">索引</th>
                <th scope="col">匹配分</th>
                <th scope="col">型号</th>
                <th scope="col">发动机</th>
                <th scope="col">年份</th>
                <th scope="col">价格</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(cars, index) in search_results" :key="index">
                <td>{{ index }}</td>
                <td>{{ cars._id }}</td>
                <td>{{ cars._index }}</td>
                <td>{{ cars._score }}</td>
                <td>{{ cars._source.name }}</td>
                <td>{{ cars._source.engine }}</td>
                <td>{{ cars._source.year }}</td>
                <td>{{ cars._source.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { searchCars } from "@/api/cars";

export default {
  name: "SearchPage",
  props: {
    msg: String,
  },
  data() {
    return {
      message: "",
      search_data: "",
      search_results: "",
      showMessage: false,
      selected: null,
      options: [
        { value: null, text: "请选择搜索模式" },
        { value: "a", text: "固定分数查询" },
        { value: "b", text: "布尔查询" },
        { value: "c", text: "更多查询" },
      ],
    };
  },
  methods: {
    onSearch(e) {
      e.preventDefault();
      const data = this.search_data;
      console.log(data);
      const payload = {
        input: data,
      };
      this.getCars(payload);
    },
    getCars(query) {
      searchCars(query)
        .then((res) => {
          console.log(res);
          this.search_results = res.data.infos.hits.hits;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
