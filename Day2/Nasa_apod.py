import json
nasa_apod_data = '''
{
    "copyright": "Gianni Sarcone",
    "date": "2024-09-14",
    "explanation": "Only natural colors of the Moon in planet Earth's sky appear in this creative visual presentation. Arranged as pixels in a framed image, the lunar disks were photographed at different times. Their varying hues are ultimately due to reflected sunlight affected by changing atmospheric conditions and the alignment geometry of Moon, Earth, and Sun. Here, the darkest lunar disks are the colors of earthshine. A description of earthshine, in terms of sunlight reflected by Earth's oceans illuminating the Moon's dark surface, was written over 500 years ago by Leonardo da Vinci.  But stand farther back from your screen or just shift your gaze to the smaller versions of the image. You might also see one of da Vinci's most famous works of art.  Tonight: International Observe the Moon Night",
    "hdurl": "https://apod.nasa.gov/apod/image/2409/Moonalisa_base_corr.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "The Moona Lisa",
    "url": "https://apod.nasa.gov/apod/image/2409/Moonalisa_Example1024.jpg"
}
'''

apod = json.loads(nasa_apod_data)

print("Title:", apod["title"])
print("Explanation:", apod["explanation"])
