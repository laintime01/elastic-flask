import requests from "@/request";

export function searchCars(query) {
  return requests({
    url: "/get_es",
    method: "get",
    params: query,
  });
}
