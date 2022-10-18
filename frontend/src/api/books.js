import request from "@/request/request";

export function searchBooks(query) {
  return request({
    url: "/books",
    method: "post",
    data: query,
  });
}
