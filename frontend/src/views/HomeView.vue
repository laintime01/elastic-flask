<template>
  <div class="home">
    <SearchPage msg="ElasticSearch-Flask" />
  </div>
</template>

<script>
// @ is an alias to /src
import SearchPage from "@/components/SearchPage.vue";

export default {
  name: "HomeView",
  components: {
    SearchPage,
  },
};
</script>
