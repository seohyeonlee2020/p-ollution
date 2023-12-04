
def loadMapofKorea():
    korea_provinces = gpd.read_file('/Users/seohyeonlee/p-ollution/data/korea_provinces.json')
    province_fullname = korea_provinces['name_eng']
    #print(province_fullname)
    province_short = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Sejong', 'Gyeonggi', 'Gangwon', 'Choongbuk', 'Choongnam', 'Jeonbuk', 'Jeonnam', 'Gyeongbuk', 'Gyeongnam', 'Jeju' ]
    province_name_conversion = dict(zip(province_fullname, province_short))
    
    #id for base and choropleth map
    korea_provinces['province'] = pd.Series(province_short)
    korea_province_map = korea_provinces[["province", "geometry"]].set_index("province")
    print(korea_province_map.index)

    return korea_province_map

def add_choropleth_to_basemap(base_map, pollutant_data, pollutant_name, your_map):
    # 망원시장 37.5560° N, 126.9064° E
    #print(data_dict[pollutant])
    Choropleth(geo_data=your_map.__geo_interface__, 
            data=pollutant_data, 
            key_on="feature.id", 
            fill_color='YlGnBu', 
            legend_name=pollutant_name,
            ).add_to(base_map)
    base_map
    return base_map


loadMapofKorea()