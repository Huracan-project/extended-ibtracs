# Extended IBTrACS
A database extending the IBTrACS database of best-track tropical cyclones with (re)analyses information.

The database is currently based on IBTrACS data in the North Atlantic. It is easy to extend to other basins, and can be done on request, or by yourself tweaking the provided scripts. No filtering is done a priori on the IBTrACS tracks. In other words, any track, however weak, short or old is included as long as it was in IBTrACS in the first place. You may perform your own filtering as a post-treatment if necessary (e.g. select only cyclones that reached a given category, etc.).

Currently includes data from:
* ERA20C (ECMWF's 20th century reanalysis) tracked with TRACK over 1901-2021
* ERA5 (ECMWF's contemporary reanalysis) tracked with TRACK over 1940-2022 and SyCLoPS over 1979-2022
* JRA3Q (JMA's contemporary reanalysis) tracked with TRACK over 1948-2023
* ECMWF Operational Analysis (ECMWF-OP-AN) since 2006

Note that the temporal coverage is different for each of the datasets. The ECMWF's operational analysis is also inhomogeneous with time by itself, as resolution and assimilation systems changed over time.

It is easy to add any other track dataset as long as the tracks are already tracked. Ideally, this tracking should include any cyclone track regardless of nature (i.e. no TC identfication criterion has been applied) as the IBTrACS matching will take care of identification. To provide added value, it is desirable that the tracking provides tracks that last for longer than they do in IBTrACS. If the point is to add more/better information to track over their recorded lifecycle, it is likely preferable to retrieve this information using IBTrACS tracks in the first place.

For information about how the database is constructed, please see the `create_extended_ibtracs` notebook.

Several additional extensions are provided, which include more data. Feel free to use the scripts to create a version that suits best your needs depending on what you need to add. These extensions include: 
* Addition of attributes from IBTrACS;
* Addition of translation speed and direction;
* Addition of CPS parameters from ERA5 and JRA3Q;

Miscellanous notes:
* Winds are provided in m/s.
* Pressures are provided in hPa.

TODO: 
* Scripts creating/adding data
* Scripts for exploring the database
* FAQ: Filtering the data, subsetting a region, etc.

**Acknowledgments**:
This project obviously builds on the essential work carried on at NOAA curating the IBTrACS database. 
IBTrACS is available at https://www.ncei.noaa.gov/products/international-best-track-archive, see also important references therein. 