
import requests
import json
import time

API_KEY = 'AIzaSyAsxQKaKDfrCTqMvFEdEkACH0nhGpZQhmI'
channel_ids = ['UCX6OQ3DkcsbYNE6H8uQQuVA', 'UCq-Fj5jknLsUf-MWSy4_brA', 'UCbCmjCuTUZos6Inko4u57UQ', 'UCpEhnqL0y41EpW2TvWAHD7Q', 'UCvlE5gTbOvjiolFlEm-c_Ow', 'UCk8GzjMOrta8yxDcKfylJYw', 'UCJplp5SjeGSdVdwsfb9Q7lQ', 'UCbp9MyKCTEww4CxEzc_Tp0Q', 'UCFFbwnve3yF62-tVXkTyHqg', 'UC-lHJZR3Gqxm24_Vd_AJ5Yw', 'UCJ5v_MCY6GNUBTO8-D3XoAg', 'UCiVs2pnGW5mLIc1jS2nxhjg', 'UCyoXW-Dse7fURq30EWl_CUA', 'UC6-F5tO8uklgE9Zy8IvbdFw', 'UCOmHUn--16B90oW2L6FRR3A', 'UCBnZ16ahKA2DZ_T5W0FPUXg', 'UC5gxP-2QqIh_09djvlm9Xcg', 'UCppHT7SZKKvar4Oc9J4oljQ', 'UCcdwLMPsaU2ezNSJU1nFoBQ', 'UC-oXnP23X5dNclQUF6KspHw', 'UC295-Dw_tDNtZXFeAPAW6Aw', 'UC55IWqFLDH1Xp7iu1_xknRA', 'UCLkAepWjdylmXSltofFvsYQ', 'UCrnQFuUabBHaw-BRhPo8xEA', 'UC3IZKseVpdzPSBaWxBxundA', 'UCaayLD9i5x4MmIoVZxXSv_g', 'UCJrDMFOdv1I2k8n9oK_V21w', 'UCgFXm4TI8htWmCyJ6cVPG_A', 'UCIwFjwMjI0y7PDBVEO9-bkQ', 'UCtxD0x6AuNNqdXO9Wp5GHew', 'UCL5nlHWXVLeOsSjKH2fhmsg', 'UCt4t-jeY85JegMlZ-E5UWtA', 'UCP6uH_XlsxrXwZQ4DlqbqPg', 'UC1ciY6kR3yj3kaKZ6R7ewAg', 'UCK1i2UviaXLUNrZlAFpw_jA', 'UCY1kMZp36IQSyNx_9h4mpCg', 'UCe9JSDmyqNgA_l2BzGHq1Ug', 'UCffDXn7ycAzwL2LDlbyWOTw', 'UCoQm-PeHC-cbJclKJYJ8LzA', 'UCPuEAY09CtdTzFNWuqVZgDw', 'UC56gTxNs4f9xZ7Pa2i5xNzg', 'UCbTLwN10NoCU4WDzLf1JMOA', 'UCbuK8xxu2P_sqoMnDsoBrrg', 'UCfM3zsQsOnfWNUppiycmBuw', 'UCZs0WwC0Dn_noiQE2BHSTKg', 'UC3gNmTGu-TTbFPpfSs5kNkg', 'UC4JCksJF76g_MdzPVBJoC3Q', 'UCOnIJiQuk1fDSp6p1GCZy3A', 'UCe881NhQWMtkQ2Qfm2Vk8Jg', 'UCRijo3ddMTht_IHyNSNXpNQ', 'UCqECaJ8Gagnn7YCbPEzWH6g', 'UC4wEPe5mrHGAUjjTfXH_C-Q', 'UC4NALVCmcmL5ntpV0thoH6w', 'UCF1JIbMUs6uqoZEY1Haw0GQ', 'UC0Wju2yvRlfwqraLlz5152Q', 'UCyagEfIN1okQ-s996XAqCFQ', 'UCEdvpU2pFRCVqU6yIPyTpMQ', 'UCRx3mKNUdl8QE06nEug7p6Q', 'UCMgapddJymOC6MBOiOqia1A', 'UClmXPfaYhXOYsNn_QUyheWQ', 'UCqJ5zFEED1hWs0KNQCQuYdQ', 'UC3MLnJtqc_phABBriLRhtgQ', 'UCXbYlU08sOTBktOtjVsvR6w', 'UC9CoOnJkIBMdeijd9qYoT_g', 'UC-LPIU24bQXVljUXivKEeRQ', 'UCiGm_E4ZwYSHV3bcW1pnSeQ', 'UCVNouUw3d3l5JYVCxhAQXKA', 'UC_A7K2dXFsTMAciGmnNxy-Q', 'UCJg19noZp7-BYIGvypu_cow', 'UCvh1at6xpV1ytYOAzxmqUsA', 'UCYiGq8XF7YQD00x7wAd62Zg', 'UCwI5Sc0AC2NQrc-aU5W-QmQ', 'UCstEtN0pgOmCf02EdXsGChw', 'UCgKEvLp8DXCTMq4QY6wW7bw', 'UC_gV70G_Y51LTa3qhu8KiEA', 'UC6gVx_vALsYT-z_u1djJbBQ', 'UCwHE1kM1CPJd_pI9FQ0-4dg', 'UCEeEQxm6qc_qaTE7qTV5aLQ', 'UCQ7x25F6YXY9DvGeHFxLhRQ', 'UC4-79UOlP48-QNGgCko5p2g', 'UCmBA_wu8xGg1OfOkfW13Q0Q', 'UCWi_65E_L8tQZ34C6wVAlpQ', 'UCo6y9hnRawAqtyWhRhblXqg', 'UCV4xOVpbcV8SdueDCOxLXtQ', 'UCzoUWqjCbcfWFdOMvoep8FA', 'UC4tS4Q_Cno5JVcIUXxQOOpA', 'UC1a2ZCw7tugRZYRMnecNj3A', 'UCYLNGLIzMhRTi6ZOLjAPSmw', 'UCRWFSbif-RFENbBrSiez1DA', 'UCKe6w0exI94U-RzqAyoY1VA', 'UCNzmmbXIbMzlqE8nD1PBXfg', 'UCRm96I5kmb_iGFofE5N691w', 'UCIPPMRA040LQr5QPyJEbmXA', 'UCttspZesZIDEwwpVIgoZtWQ', 'UCYWOjHweP2V-8kGKmmAmQJQ', 'UCV306eHqgo0LvBf3Mh36AHg', 'UCj-SWZSE0AmotGSQ3apROHw', 'UCOsyDsO5tIt-VZ1iwjdQmew', 'UCJrOtniJ0-NWz37R30urifQ', 'UCQZfFRohQ7UX-0CdXl-6pwQ', 'UCgJ5_1F6yJhYLnyMszUdmUg', 'UCtW7qWjpCZ8zps-Cf2NF26w', 'UCK5Q72Uyo73uRPk8PmM2A3w', 'UCj0O6W8yDuLg3iraAXKgCrQ', 'UCw7xjxzbMwgBSmbeYwqYRMg', 'UCX8pnu3DYUnx8qy8V_c6oHg', 'UCYvmuw-JtVrTZQ-7Y4kd63Q', 'UCsSsgPaZ2GSmO6il8Cb5iGA', 'UCqq5n-Oe-r1EEHI3yvhVJcA', 'UCSiDGb0MnHFGjs4E2WKvShw', 'UCdX5KXiCTPYWYZscfphgQ4g', 'UCj22tfcQrWG7EMEKS0qLeEg', 'UC3KQ5GWANYF8lChqjZpXsQw', 'UC4rlAVgAK0SGk-yTfe48Qpw', 'UCECJDeK0MNapZbpaOzxrUPA', 'UC5c9VlYTSvBSCaoMu_GI6gQ', 'UCzEAWIWMigRBbulQ6yVlilg', 'UCcgqSM4YEo5vVQpqwN-MaNw', 'UCLsooMJoIpl_7ux2jvdPB-Q', 'UCS94J1s6-qc8v7btCdS2pNg', 'UCK9F8nycURBsR0YlrBsu1Ag', 'UCZJ7m7EnCNodqnu5SAtg8eQ', 'UCmL1WlDI8UkXDXCXcBQN9CA', 'UCQ8cXCAuUgXFt4TWcS8ouXA', 'UC4hGmH5sABOA70D4fGb8qNQ', 'UCz7PhJtc2G8Sre2vCLfmqAw', 'UCNRl8nOCoUvki2FNFxQZgEg', 'UCBR8-60-B28hp2BmDPdntcQ', 'UCyI6QRxXArFsfWlMdvoG2hw', 'UC8f7MkX4MFOOJ2SerXLInCA', 'UCsT0YIqwnpJCM-mx7-gSA4Q', 'UC3ZkCd7XtUREnjjt3cyY_gg', 'UCq8DICunczvLuJJq414110A', 'UC2bYhAHyaqfWlPXWBVk4BcA', 'UCaHEdZtk6k7SVP-umnzifmQ', 'UCNUQK9mQoqi4yNXw2_Rj6SA', 'UCuSo4gcgxJRf4Bzu43wwVyg', 'UCwQCMGALOA_sfJ2YXEnlHkw', 'UCx790OVgpTC1UVBQIqu3gnQ', 'UCM9r1xn6s30OnlJWb-jc3Sw', 'UCbGPgvNunvclTypPtL3sa0w', 'UCKAqou7V9FAWXpZd9xtOg3Q', 'UCSf0s2ogUVYpJPuzW1zpAOg', 'UCe3yZzUwpmy2eKKmF9svX0Q', 'UCoUM-UJ7rirJYP8CQ0EIaHA', 'UCIvaYmXn910QMdemBG3v1pQ', 'UCpYye8D5fFMUPf9nSfgd4bA', 'UCJdWU3_aflA-cPLfb81SeqQ', 'UCXazgXDIYyWH-yXLAkcrFxw', 'UCunqjMN6EEbXjzU-RvwJrig', 'UCN8S4CqMRy6tVKVXvs7Bzeg', 'UCAOtE1V7Ots4DjM8JLlrYgg', 'UC9TO_oo4c_LrOiKNaY6aysA', 'UCWsDFcIhY2DBi3GB5uykGXA', 'UCJfNJmcv6LXCDsaa2kB_-7A', 'UCZuPJZ2kGFdlbQu1qotZaHw', 'UCcvNYxWXR_5TjVK7cSCdW-g', 'UCb2HGwORFBo94DmRx4oLzow', 'UChGJGhZ9SOOHvBB0Y4DOO_w', 'UCEKWXRsfUHkan-D_ljU8Asw', 'UCm-Qr3k89gtXcuv2jL29XFw', 'UC4DLvb5xZ9OLcVM1KC_R97g', 'UCKL5hAuzgFQsyrsQKgU0Qng', 'UCeYTfGpNCmVhlxjQxBDrGPA', 'UC5tuYcCdiKuF5Y2ZonuarwA', 'UCjp_3PEaOau_nT_3vnqKIvg', 'UC56D-IHcUvLVFTX_8NpQMXg', 'UCe6n0z9UbsxYCS8P83f84tw', 'UCp0hYYBW6IMayGgR-WeoCvQ', 'UCVRqK0tS3B8pVog1HwCR4pg', 'UCBAb_DK4GYZqZR9MFA7y2Xg', 'UCtiddfzHXNevG-yYe5vc_4Q', 'UC0WP5P-ufpRfjbNrmOWwLBQ', 'UCwVg9btOceLQuNCdoQk9CXg', 'UCsPF3cApzCohxPp5oKdoWSQ', 'UCBVjMGOIkavEAhyqpxJ73Dw', 'UCR1hQY5sz5NEYofdv09XimA', 'UCjIA3wwhi0QjSOXAZwOXbPA', 'UC7_YxT-KID8kRbqZo7MyscQ', 'UCbomPUMyPHCgrqD5iYnzj1A', 'UCgwv23FVv3lqh567yagXfNg', 'UCHUu2HAnogpaK2UmTSJT8jg', 'UCFMFB7_Ik8jBnCwSuh295wA', 'UCPCaXSwaos-QI03iZtx8I6g', 'UCmzDf_a7CCFuxos7hspcWRQ', 'UC6VAIqNQBc7ggiqvsOHOBqw', 'UCEv344Oza4sx0QmNMKL-w6g', 'UCesDcQvvaerfrFF-7RAzGZg', 'UCWaOde99oeUVoXbIj3SNu9g', 'UCwD4x63A9KC7Si2RuSfg-SA', 'UCBOmfqgTZi7yDp4-3Lr_3lA', 'UClFN9LShD_Pv0wnSeUKbUZw', 'UCUMxxg0KvWiSWHUXRPpnKzw', 'UC2fvyma9iKsjN9EZW_FWW1A', 'UCX_uPA_dGf7wXjuMEaSKLJA', 'UClZF7OsrECe3t_ADrjZEh_Q', 'UC48h7Dst_hX82HxOf3xJw_w', 'UCN4NflpHqLeHQZ91kTUVCBw', 'UCm1hOHNgH6x8MF22676CmZA', 'UCUaT_39o1x6qWjz7K2pWcgw', 'UCt4atlExw8aj3Bm79nv1fig', 'UCHvoq_rGmOKJKGId1nD1V4Q', 'UCPNxhDvTcytIdvwXWAm43cA', 'UCe5l8ZbCMva0D6caxIu-28Q', 'UCX52tYZiEh_mHoFja3Veciw', 'UCNApqoVYJbYSrni4YsbXzyQ', 'UCb8vrqP8Z7Oz9ZTYvUtjUHQ', 'UCu7Hg0f3rxqZ6qs-188ZbjQ', 'UCOF23vGxkbhN4wl7ROrgXsA', 'UCDwhsmzFDLc5hOB6SUglAjg', 'UCpB959t8iPrxQWj7G6n0ctQ', 'UCWw-Guyr5ul9B-d5kJlHMng', 'UC_82tbyeBHSaDbL725LMlvw', 'UCozwejESfvl88CBBL0KgEhw', 'UCEwIUtFBhaI2L2PuKv0KL2g', 'UCHcn4Ux-sO9nzNu7rDsoQLg', 'UCs530WBGoJwN567Ntjwz2jQ', 'UCi3onjs7UU2Z64i3RrVci-Q', 'UCPP3etACgdUWvizcES1dJ8Q', 'UCam8T03EOFBsNdR0thrFHdQ', 'UCP84QWij0alw4MvzqzyfOnw', 'UCVtD5iA4rUuOK5cQrB_o4ow', 'UCw5laSluKZol8QuE1fOToTQ', 'UCLtNvbkqea8wN_kGtfgx_Mw', 'UCNzsYU0aWwjERj-9Y9HUEng', 'UC_aEa8K-EOJ3D6gOs7HcyNg', 'UCbTVTephX30ZhQF5zwFppBg', 'UCRUhZVAUH4JyWUFmxm5P6dQ', 'UC4zWG9LccdWGUlF77LZ8toA', 'UCubB4RJhGFvqfP5z5t7Q0cQ', 'UCjvgGbPPn-FgYeguc5nxG4A', 'UCUe6ZpY6TJ0no8jI4l2iLxw', 'UCTheFErn4MureanSiqgKIag', 'UCx8Z14PpntdaxCt2hakbQLQ', 'UCebC4x5l2-PQxg46Ucv9CsA', 'UCYqOeAXJm8yV9sJ8Ud3cR7A', 'UCQ8TuCvcDMepleXFyOQfyOQ', 'UCNvYCW3cMbkWy2g2v4Wb6xw', 'UCEf_Bc-KVd7onSeifS3py9g', 'UCoIOOL7QKuBhQHVKL8y7BEQ', 'UC56cowXhoqRWHeqfSJkIQaA', 'UCY-at5vWhDoMJ8y0kIPFwDA', 'UCozAuGJZ5MPoijz8IE_1Gtw', 'UC371icpvZj2oQaocL0i9L-g', 'UCT9zcQNlyht7fRlcjmflRSA', 'UCm3hAp1m1xlAz0ve_EKAo4g', 'UC9tadWDByHo4_op_O7v111g', 'UCI78AdiI6f7VKhqW1i4B3Rw', 'UCbCJmNKAL85O1VFeD6Wj60g', 'UCLYqpLGnCoQfcD7BdDKsSxQ']

# Function to fetch data for up to 50 channels at a time
def fetch_channel_stats(ids):
    url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
        'part': 'snippet,statistics',
        'id': ','.join(ids),
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed request: HTTP {response.status_code}")
        return {}

# Gather all channel stats
all_stats = []

for i in range(0, len(channel_ids), 50):
    batch = channel_ids[i:i+50]
    result = fetch_channel_stats(batch)
    for item in result.get('items', []):
        stats = {
            "channel_id": item['id'],
            "channel": item['snippet']['title'],
            "icon": item['snippet']['thumbnails']['high']['url'],
            "subscribers": int(item['statistics'].get('subscriberCount', 0)),
            "videos": int(item['statistics'].get('videoCount', 0)),
            "channel_url": f"https://www.youtube.com/channel/{item['id']}",
            "views": int(channel_data["statistics"].get("viewCount", 0))
        }
        all_stats.append(stats)
    time.sleep(1)

# Sort by subscriber count
all_stats.sort(key=lambda x: x['subscribers'], reverse=True)

# Add ranking
for idx, item in enumerate(all_stats, 1):
    item['ranking'] = idx

# Save to JSON
with open("top_youtube_channels_stats.json", "w") as f:
    json.dump(all_stats, f, indent=2)
