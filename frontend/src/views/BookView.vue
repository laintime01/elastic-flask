<template>
  <div class="jumbotron">
    <h1>ElasticSearch-Flask Demo</h1>
    <p>Program Book查询页面,<br /></p>
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
            <b-form-input
              placeholder="请输入查询关键字"
              v-model="search_data"
              class="search-box"
              @keyup="onSearch"
            >
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
                <th scope="col">Id</th>
                <th scope="col">Title</th>
                <th scope="col">Reviews</th>
                <th scope="col">Rating</th>
                <th scope="col">Description</th>
                <th scope="col">Pages</th>
                <th scope="col">Type</th>
                <th scope="col">Price</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(books, index) in search_results" :key="index">
                <td>{{ index }}</td>
                <td>{{ books._source.Book_title }}</td>
                <td>{{ books._source.Reviews }}</td>
                <td>{{ books._source.Rating }}</td>
                <td>{{ books._source.Description }}</td>
                <td>{{ books._source.Page_Number }}</td>
                <td>{{ books._source.Type }}</td>
                <td>{{ books._source.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { searchBooks } from "@/api/books";
import $ from "jquery";

export default {
  name: "BookView",
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
      const payload = {
        input: data,
      };
      this.getBooks(payload);
    },
    getBooks(query) {
      searchBooks(query)
        .then((res) => {
          console.log(res);
          this.search_results = res.data.hits.hits;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    AutoComplete() {
      // eslint-disable-next-line no-unused-vars
      let debounce;
      $(".search-box").on("keydown", function () {
        const data = $(".search-box").val();
        console.log(data);
        const payload = {
          input: data,
        };
        console.log(payload);
        searchBooks(payload)
          .then((res) => {
            console.log(res);
            this.search_results = res.data.infos.hits.hits;
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
