  curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{
    "resource": "/hello",
    "path": "/vits_onnx/raw/tts",
    "httpMethod": "POST",
    "multiValueQueryStringParameters":{
      "text":"[JA]こんにちは。[JA][ZH]你好。[ZH]"

    },
    "pathParameters": {
    },
     "requestContext": { 
      "httpMethod": "POST"
    },
    "body": "{\"sid\":2,\"g2pConfig\":{\"cleanner_name\":\"japanese_cleaners2\",\"symbols\":[\"_\",\",\",\".\",\"!\",\"?\",\"-\",\"~\",\"\u2026\",\"A\",\"E\",\"I\",\"N\",\"O\",\"Q\",\"U\",\"a\",\"b\",\"d\",\"e\",\"f\",\"g\",\"h\",\"i\",\"j\",\"k\",\"m\",\"n\",\"o\",\"p\",\"r\",\"s\",\"t\",\"u\",\"v\",\"w\",\"y\",\"z\",\"\u0283\",\"\u02a7\",\"\u02a6\",\"\u2193\",\"\u2191\",\"\"],\"text\":\"こにちわ、あやせさん\"}}"
}'
