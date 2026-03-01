"""
短视频解析 API
支持抖音、快手、视频号解析
"""
from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Video解析API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Video解析API", "endpoints": ["/parse"]}

@app.get("/parse")
def parse_video(url: str = Query(..., description="视频链接")):
    """解析视频链接"""
    # 模拟解析返回
    return {
        "success": True,
        "url": url,
        "title": "示例视频标题",
        "author": "作者名称",
        "likes": 1234,
        "comments": 56,
        "share_url": "https://example.com/video.mp4"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
