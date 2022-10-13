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
