本專案提供台灣便利超商營業處的抓取程式

檔案結構：

* [data]
	* city_7_11.dat 預抓好的資料
	* city_family.dat 預抓好的資料
* [doc]
* [model]
	* models.py 7-11 內部模型類別
	* FamilyModel.py 全家內部模型類別
* [example]
	* load_data.py 讀入營業處資料
* crawler_7-11.py 7-11 的營業處資料抓取，預設資料存到[city_7_11.dat](data/city_7_11.data)
* crawler_family.py 全家的營業處資料抓取，預設資料存到[city_family.dat](data/city_family.data)
