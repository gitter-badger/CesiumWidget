simple_czml = r"""
[
{ "id":"document", "version":"1.0" } ,
{
  "id": "InternationalSpaceStation",
  "position": {
    "referenceFrame": "INERTIAL",
    "epoch": "2012-05-02T12:00:00Z",
    "cartesian": [
      0.0, -6668447.2211117, 1201886.45913705, 146789.427467256,
      60.0, -6711432.84684144, 919677.673492462, -214047.552431458,
      90.0, -6721319.92231553, 776899.784034099, -394198.837519575,
      150.0, -6717826.447064, 488820.628328182, -752924.980158179,
      180.0, -6704450.41462847, 343851.784836767, -931084.800346031,
      240.0, -6654518.44949696, 52891.726433174, -1283967.69137678
    ],
    "nextTime": 300.0,
    "interpolationAlgorithm": "LAGRANGE",
    "interpolationDegree": 5
  }
},
{
    "id":"/Application/STK/Scenario/simple/Facility/AGI",
    "label":{
      "fillColor":{
        "rgba":[
          0,255,255,255
        ]
      },
      "font":"10pt Lucida Console",
      "horizontalOrigin":"LEFT",
      "outlineColor":{
        "rgba":[
          0,0,0,255
        ]
      },
      "pixelOffset":{
        "cartesian2":[
          12.0,0.0
        ]
      },
      "scale":1.0,
      "show":true,
      "style":"FILL",
      "text":"AGI",
      "verticalOrigin":"CENTER"
    },
    "position":{
      "cartesian":[
        1216469.9357990976,-4736121.71856379,4081386.8856866374
      ]
    }
  }

]"""