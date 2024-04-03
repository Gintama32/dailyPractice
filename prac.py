import os
import googleapiclient.discovery
from dotenv import load_dotenv
load_dotenv()
# Set up the API key
api_key =   os.getenv("API_KEY")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Create a function to search for videos on YouTube
def search_youtube(query):
    # Initialize the YouTube Data API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Call the search.list method to search for videos
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=5 # You can adjust the number of results as per your requirement
    )

    # Execute the request and get the response
    response = request.execute()

    # Extract video information from the response
    videos = []
    for item in response["items"]:
        video = {
            "title": item["snippet"]["title"],
            "video_id": item["id"]["videoId"],
            "channel": item["snippet"]["channelTitle"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        videos.append(video)

    return videos

# Example usage
if __name__ == "__main__":
    query = input("Enter the search query: ")
    search_results = search_youtube(query)

    # Print search results
    for i, video in enumerate(search_results, 1):
        print(f"{i}. Title: {video['title']}")
        print(f"   Channel: {video['channel']}")
        print(f"   URL: {video['url']}")
        print()