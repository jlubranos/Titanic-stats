function optionClick(selection) {
    d3.json(`/statistics/${selection}`).then((response)=> {
// Response received from app.py according the user selection...
// Create and display Bar Chart for female and males by class and survival status
      if (response.length>0) {
            var trace1 = {
              x: ['Deceased', 'Survived'],
              y: [response[0].count, response[1].count],
              width:.2,
              name: 'Females',
              marker:{
                color: ['#ff99cc', '#ff99cc'],
              },              
              type: 'bar'
            };
            
            var trace2 = {
              x: ['Deceased', 'Survived'],
              y: [response[2].count, response[3].count],
              width:.2,
              name: 'Male',
              marker:{
                color: ['#99ccff', '#99ccff'],
              },
              type: 'bar'
            };
            
            var data = [trace1, trace2];
            
            var layout = {
              barmode: 'group',
              bargap:0.25,
              bargroupgap:0.1,
              title:"Titanic Passenger Statistics by Gender and Class ("+ selection+" Class)",
              plot_bgcolor:'rgba(0,0,0,0.5)',
              paper_bgcolor:'rgba(0,0,0,0.5)',
              font:{
                color:'#ffffff',
                size:10
              },
              yaxis: {
                title:'Count',
                color:'#ffffff'
              },
            };
 
            var config = {
              responsive: true
              };
 
              Plotly.newPlot("hist",data, layout,config);
        }
    });
}