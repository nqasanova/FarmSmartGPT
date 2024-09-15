var aoi = ee.Geometry.Polygon([
    [
      [48.2517, 40.085],    // Upper left
      [48.7503, 40.085],    // Upper right
      [48.7503, 39.7533],   // Lower right
      [48.2564, 39.7589]    // Lower left
    ]
  ]);
  
  var sentinel2 = ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
      .filterBounds(aoi)  // Use 'aoi' instead of 'region'
      .filterDate('2020-01-01', '2022-12-31')
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20));  // Filter for less cloudy images
      
  var composite = sentinel2.median();
  
  var visParams = {
      min: 0,
      max: 3000,
      bands: ['B4', 'B3', 'B2']  // Red, Green, Blue bands for natural color
  };
  
  // Center the map on the AOI
  Map.centerObject(aoi, 10);
  Map.addLayer(composite, visParams, 'Sentinel-2 Composite');
  
  // Export the image to Google Drive
  Export.image.toDrive({
      image: composite,
      description: 'Sentinel2_AOI',
      scale: 10,  // 10-meter resolution for Sentinel-2
      region: aoi,  // Use 'aoi' instead of 'region'
      fileFormat: 'GeoTIFF'
  });