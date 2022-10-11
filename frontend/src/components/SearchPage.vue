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
          <b-input-group style="float: left; width: 30%">
            <b-input-group-prepend is-text>
              <b-icon icon="search"></b-icon>
            </b-input-group-prepend>
            <b-form-input placeholder="请输入查询关键字" v-model="search_data">
            </b-form-input>
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
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">Year</th>
                <th scope="col">Price</th>
                <th scope="col">Km</th>
                <th scope="col">Fuel</th>
                <th scope="col">Seller</th>
                <th scope="col">Owner</th>
              </tr>
            </thead>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchPage",
  props: {
    msg: String,
  },
  data() {
    return {
      message: "",
      search_data: "",
      showMessage: false,
    };
  },
  methods: {
    onSearch() {
      console.log(this.search_data);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
