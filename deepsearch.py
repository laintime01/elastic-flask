# 精准查找
def termSearch(key, value):
    query = {
        "query": {
            "constant_score": {
                "filter": {
                    key: value
                }
            }
        }
    }
    return query


# 组合过滤
def boolSearch(should, must, must_not):
    query = {
        "query": {
            "filtered": {
                "filter": {
                    "bool": {
                        "should": should,
                        "must": must,
                        "must_not": must_not
                    }
                }
            }
        }
    }
    return query


# 查找多个精准 term and terms means contain not equals
def multipleSearch(key, value):
    query = {
        "query": {
            "constant_score": {
                "filter": {
                    # 这里是terms不是term
                    "terms": {
                        key: value
                    }
                }
            }
        }
    }
    return query


# 范围查询
def rangeSearch(key, value):
    query = {
        "query": {
            "constant_score": {
                "filter": {
                    "range": {
                        key: value
                    }
                }
            }
        }
    }
    return query


# multi_match 查询
def multi_match_search(query, type_arg, fields, tie_breaker, minimum_match):
    multi_query = {
        "multi_match": {
            "query": query,
            "type": type_arg,
            "fields": fields,
            "tie_breaker": tie_breaker,
            "minimum_should_match": minimum_match
        }
    }
    return multi_query


# 跨字段实体搜索
def cross_fields_search(query, fields):
    cross_fields = {
        "query":{
            "multi_match": {
                "query": query,
                "type": "most_fields",
                "fields": fields
            }
        }
    }
    return cross_fields


# 短语匹配
def phrase_search(key, value):
    query = {
        "query": {
            "match_phrase": {
                key: value
            }
        }
    }
    return query