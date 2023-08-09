import os
import string

import requests


def get_linkedin_data(url) -> string:
    # return "{'public_identifier': 'bao-loc-tong-a523372a', 'profile_pic_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/person/bao-loc-tong-a523372a/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230806%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230806T103919Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d7a57c9ee4788ac5551892df0d78507e564021b0a2a4a89dedfa84c146549aa7', 'background_cover_image_url': None, 'first_name': 'Bao Loc', 'last_name': 'Tong', 'full_name': 'Bao Loc Tong', 'follower_count': None, 'occupation': 'Software Engineer at PTN Global ', 'headline': 'Software Engineer at PTN Global', 'summary': None, 'country': 'VN', 'country_full_name': 'Vietnam', 'city': None, 'state': None, 'experiences': [{'starts_at': {'day': 1, 'month': 3, 'year': 2020}, 'ends_at': None, 'company': 'PTN Global ', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/ptn-global/', 'title': 'Software Engineer', 'description': None, 'location': 'Vietnam', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/ptn-global/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230806%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230806T103919Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=52fd6f9ba270b0661e8baed13e11d8887419415bc8cfeb84eb527d769e4a7a6a'}, {'starts_at': {'day': 1, 'month': 9, 'year': 2017}, 'ends_at': {'day': 1, 'month': 3, 'year': 2020}, 'company': 'FPT Software', 'company_linkedin_profile_url': 'https://www.linkedin.com/company/fpt-software/', 'title': 'Java Developer', 'description': None, 'location': 'Vietnam', 'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/fpt-software/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230806%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230806T103919Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=2fa49529cf1c557faec8b339cb2a2a94e6f5291acbbd4dac8eb8dad956e1aef2'}], 'education': [], 'languages': [], 'accomplishment_organisations': [], 'accomplishment_publications': [], 'accomplishment_honors_awards': [], 'accomplishment_patents': [], 'accomplishment_courses': [], 'accomplishment_projects': [], 'accomplishment_test_scores': [], 'volunteer_work': [], 'certifications': [{'starts_at': {'day': 1, 'month': 8, 'year': 2021}, 'ends_at': None, 'name': 'Microsoft Certified: Azure Fundamentals', 'license_number': None, 'display_source': 'credly.com', 'authority': 'Microsoft', 'url': 'https://www.credly.com/badges/4a4001ee-9efe-4c71-ad0a-8e0334354c10?source=linked_in_profile'}, {'starts_at': {'day': 1, 'month': 8, 'year': 2019}, 'ends_at': None, 'name': 'Oracle Certified Associate, Java SE 8 Programmer', 'license_number': None, 'display_source': 'credly.com', 'authority': 'Oracle', 'url': 'https://www.credly.com/badges/c822c966-1ac5-48cc-9cde-7dcfc51fb680?source=linked_in_profile'}, {'starts_at': {'day': 1, 'month': 5, 'year': 2023}, 'ends_at': {'day': 1, 'month': 5, 'year': 2026}, 'name': 'AWS Certified Developer – Associate', 'license_number': None, 'display_source': 'credly.com', 'authority': 'Amazon Web Services (AWS)', 'url': 'https://www.credly.com/badges/f9ad8f96-a2e9-468d-803d-b200ccb4e6da/linked_in_profile'}], 'connections': None, 'people_also_viewed': [{'link': 'https://www.linkedin.com/in/vfon98', 'name': 'Phong To', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/quangnguyenptn', 'name': 'Phương Quang Nguyễn', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/vo-si-liem-6783a3208', 'name': 'Vo Si Liem', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/le-khai-68b2921b0', 'name': 'Le Khai', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/nhut-kha-0a654b209', 'name': 'Nhut Kha', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/thái-trương-75a363244', 'name': 'Thái Trương', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/toan-nguyen-6a80b1188', 'name': 'Toan Nguyen', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/bngocnguyen94', 'name': 'Bao Ngoc Nguyen', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/ngohoangtho', 'name': 'Thọ Ngô Hoàng', 'summary': None, 'location': None}, {'link': 'https://www.linkedin.com/in/dien-le-732975175', 'name': 'DIEN LE', 'summary': None, 'location': None}], 'recommendations': [], 'activities': [], 'similarly_named_profiles': [], 'articles': [], 'groups': [], 'skills': ['.NET Framework', 'Angular', 'Java', 'HTML', 'TypeScript'], 'inferred_salary': {'min': None, 'max': None}, 'gender': None, 'birth_date': None, 'industry': None, 'extra': {'github_profile_id': None, 'twitter_profile_id': None, 'facebook_profile_id': None}, 'interests': [], 'personal_emails': [], 'personal_numbers': []}";

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin" # personal api
    # api_endpoint = "https://nubela.co/proxycurl/api/linkedin/company"  # company api, company profile url phai ket thuc bang /
    api_key = os.getenv(
        "PROXYCURL_API_KEY"
    )  # get your API key from https://nubela.co/proxycurl
    headers = {"Authorization": "Bearer " + str(api_key)}
    # company api
    # params = {
    #     'url': url,
    #     'resolve_numeric_id': 'true',
    #     'categories': 'include',
    #     'funding_data': 'include',
    #     'extra': 'include',
    #     'exit_data': 'include',
    #     'acquisitions': 'include',
    #     'use_cache': 'if-present',
    # }

    # personal api
    params = {
        "url": url,
        "fallback_to_cache": "on-error",
        "use_cache": "if-present",
        "skills": "include",
        "inferred_salary": "include",
        "personal_email": "include",
        "personal_contact_number": "include",
        "twitter_profile_id": "include",
        "facebook_profile_id": "include",
        "github_profile_id": "include",
        "extra": "include",
    }

    response = requests.get(api_endpoint, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        data = {
            k: v
            for k, v in data.items()
            if v not in ["", None, [], {}, "null", "undefined"]
               and k not in ["people_also_viewed", "certifications"]
        }

        if data.get("groups"):
            for group_dict in data["groups"]:
                group_dict.pop("profile_pic_url")

        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

#
#
# # Example usage:
# url = 'https://linkedin.com/in/bao-loc-tong-a523372a/'
# data = get_linkedin_data(url)
# print(data)

# import requests
#
# api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'
# api_key = os.getenv("PROXYCURL_API_KEY")
# header_dic = {'Authorization': 'Bearer ' + api_key}
# params = {
#     'company_domain': 'gatesfoundation.org',
#     'first_name': 'Bill',
#     'similarity_checks': 'include',
#     'enrich_profile': 'enrich',
#     'location': 'Seattle',
#     'title': 'Co-chair',
#     'last_name': 'Gates',
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=header_dic)
