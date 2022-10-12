import requests
from bs4 import BeautifulSoup
import os
import re
class API:
    def init(self, download_path):
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        self.download_path = download_path
    def gfweb(self, search_content):
        global paper_url
        search_content = re.sub('[-]', '', search_content)
        p = re.compile('\[\d+\]')
        key = p.findall(search_content)
        filename = self.download_path + '/' + str(key[0]) + '.pdf'
        url = 'https://sc.panda321.com/scholar?'
        headers = {
            'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            #         'Cookie':'HSID=AYBaM8eV1cbFRuhYC; SSID=A1SjYV0xhhMU4ZK04; APISID=5OOs2epteYTcJt0j/Am6wa83nmOyKkQoWx; SAPISID=B-u50osS_VC5pp2v/AA6qXOquLMBqs96Vx; __Secure-1PAPISID=B-u50osS_VC5pp2v/AA6qXOquLMBqs96Vx; __Secure-3PAPISID=B-u50osS_VC5pp2v/AA6qXOquLMBqs96Vx; SID=Owjy-BytkMpIQAmxZcOQs8NwpbD2-_YDsIKSmKSVbwiO2uFqAfX1ybnCCUmogbvpY7m-uA.; __Secure-1PSID=Owjy-BytkMpIQAmxZcOQs8NwpbD2-_YDsIKSmKSVbwiO2uFqIcX85Y1qOd0ByUQX1Qg8Vw.; __Secure-3PSID=Owjy-BytkMpIQAmxZcOQs8NwpbD2-_YDsIKSmKSVbwiO2uFqjc2mXpVGgG0d5s-mGaukMA.; AEC=AakniGNJvOxp6ZECRhsaIUCHMwUtc9WrjmlSWFfWTRZ9zAyw63vsV-FvVxg; 1P_JAR=2022-09-25-11; GSP=LM=1664976893:S=hXIZRphW4yz2RNjT; SIDCC=AEf-XMQrbTPxFtgMEfwW01EQtZUbEvOwHE1Ma4S0wGrQ5pKlmICtWpId5zLbGZfRfpCdcILmyw; __Secure-1PSIDCC=AEf-XMQzfzeJ-IvCmxu_gS-s4V_elFKt5KMQb3djZg5-ObkL9-9nqbYHPDlwiwxKacMN5qfzuw; __Secure-3PSIDCC=AEf-XMTq79N3ewLoe_KLHW46P8GHQ8hb2SEChDaFQW1UuKVL1bv1MkKbondnzBzvFCIwdEjWpw; NID=511=FotchhUKPOCKbIZx8euau0vyw1W8be52PyKowWAg8vEWWdBYqNrFiwDiDzmIu9gkSNvD8d6joFcgEtCFOibBAwnfFCfLdQFcxAccgSs2BSlSPOrBYw40FcwSR_eTGXbxg8q97FumBaMCRuyXYKsKBUiH_TcwzQGh5EDd79JL5KOMWXMfmy-wMYMxEZ-Qt43j96P6Wg65kaPZBMX-NC759LuW_yLQmxJr78Ulq3PNn8RLzTCaRsv70WhzCeFHAz9ZBkSzsNC1WS92q8ZMMpHFW19mgGgSjjuk',
        }
        param = {
            'hl': 'zh-CN',
            'as_sdt': '0,5',
            'q': search_content,
            'btnG': '',
        }
        if not os.path.exists(filename):
            page_text = requests.get(url=url, params=param, headers=headers).text
            soup = BeautifulSoup(page_text, 'lxml')
            try:
                paper_url = soup.select(".gs_or_ggsm > a")[2]['href']
            except:
                return(search_content[0:3] + "下载失败，请手动查看")
            paper_data = requests.get(url=paper_url, stream=True)
            with open(filename, 'wb') as fp:
                    fp.write(paper_data.content)
                    fp.close()
        return(str(key[0]) + "下载成功")


if __name__ == '__main__':
    api = API()
    api.init(download_path=r'C:\Users\Ding\Desktop\Download')
    api.gfweb(search_content='[1] Y. Bengio, P. Simard, and P. Frasconi. Learning long-term dependen-cies with gradient descent is difﬁcult. IEEE Transactions on NeuralNetworks, 5(2):157–166, 1994.')

#
# if __name__ == 'main':
# url = 'https://sc.panda321.com/scholar?'
# headers = {
#         'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# #         'Cookie':'HSID=AYBaM8eV1cbFRuhYC; SSID=A1SjYV0xhhMU4ZK04; APISID=5OOs2epteYTcJt0j/Am6wa83nmOyKkQoWx; SAPISID=B-u50osS_VC5pp2v/AA6qXOquLMBqs96Vx; __Secure-1PAPISID=B-u50osS_VC5pp2v/AA6qXOquLMBqs96Vx; __Secure-3PAPISID=B-u50osS_VC5pp2v/AA6qXOquLMBqs96Vx; SID=Owjy-BytkMpIQAmxZcOQs8NwpbD2-_YDsIKSmKSVbwiO2uFqAfX1ybnCCUmogbvpY7m-uA.; __Secure-1PSID=Owjy-BytkMpIQAmxZcOQs8NwpbD2-_YDsIKSmKSVbwiO2uFqIcX85Y1qOd0ByUQX1Qg8Vw.; __Secure-3PSID=Owjy-BytkMpIQAmxZcOQs8NwpbD2-_YDsIKSmKSVbwiO2uFqjc2mXpVGgG0d5s-mGaukMA.; AEC=AakniGNJvOxp6ZECRhsaIUCHMwUtc9WrjmlSWFfWTRZ9zAyw63vsV-FvVxg; 1P_JAR=2022-09-25-11; GSP=LM=1664976893:S=hXIZRphW4yz2RNjT; SIDCC=AEf-XMQrbTPxFtgMEfwW01EQtZUbEvOwHE1Ma4S0wGrQ5pKlmICtWpId5zLbGZfRfpCdcILmyw; __Secure-1PSIDCC=AEf-XMQzfzeJ-IvCmxu_gS-s4V_elFKt5KMQb3djZg5-ObkL9-9nqbYHPDlwiwxKacMN5qfzuw; __Secure-3PSIDCC=AEf-XMTq79N3ewLoe_KLHW46P8GHQ8hb2SEChDaFQW1UuKVL1bv1MkKbondnzBzvFCIwdEjWpw; NID=511=FotchhUKPOCKbIZx8euau0vyw1W8be52PyKowWAg8vEWWdBYqNrFiwDiDzmIu9gkSNvD8d6joFcgEtCFOibBAwnfFCfLdQFcxAccgSs2BSlSPOrBYw40FcwSR_eTGXbxg8q97FumBaMCRuyXYKsKBUiH_TcwzQGh5EDd79JL5KOMWXMfmy-wMYMxEZ-Qt43j96P6Wg65kaPZBMX-NC759LuW_yLQmxJr78Ulq3PNn8RLzTCaRsv70WhzCeFHAz9ZBkSzsNC1WS92q8ZMMpHFW19mgGgSjjuk',
# }
# search_content = 'Network in network'
# param ={
#     'hl': 'zh-CN',
#     'as_sdt': '0,5',
#     'q': search_content,
#     'btnG': '',
# }
# # data = {
# #     'kw': search_content
# # }
# page_text = requests.get(url=url, params=param, headers=headers).text
# soup = BeautifulSoup(page_text, 'lxml')
# paper_url = soup.select(".gs_or_ggsm > a")[2]['href']
# paper_data = requests.get(url=paper_url, stream=True)
# print(paper_data)
# with open(filename,'wb') as fp:
#     fp.write(paper_data.content)
#     fp.close()
# # print(soup.find('div', class_="gs_r gs_or gs_scl"))
# # print(soup.a)
# print(soup.select(".gs_or_ggsm > a")[2]['href'])
# # print(soup.find_all('div', class_='gs_rg s_or gs_scl'))
