import request from "@/request/request";

export function searchCars(query) {
  return request({
    url: "/get_es",
    method: "post",
    data: query,
  });
}
