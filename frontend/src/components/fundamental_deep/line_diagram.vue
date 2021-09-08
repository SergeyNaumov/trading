<template>
        <canvas class="diagramm"
        :width="width" 
        :height="height"
        :id="id"


    />
</template>
<script>
import Chart from '/src/javascript/chart.js' 

export default{
    props:['list','description'],
    data(){
        return {
            id: '',
            width: 300,
            height: 300,
            labels:[],
            values:[]
        }
        
    },
    created(){
        this.id='d_'+Math.random().toString(36).replace(/[^a-z]+/g, '').substr(0, 5)
        this.get_labels_and_values()
        setTimeout(
            ()=>{this.draw()},
            500
        )
    },
    methods:{
        get_labels_and_values(){
            for(let l of this.list){
                this.labels.push(l.year)
                this.values.push(l.v)
            }
        },
        draw(){
                let canvas_el=document.getElementById(this.id)
               
                let ctx = canvas_el.getContext('2d');
               
                let f=this.field
                let data=this.values
                let labels=this.labels
                let description=this.description
                
                let myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: description,
                            data: data,
                            backgroundColor: [ '#00e676'],
                            borderWidth: 1 ,
                            borderColor: '#00e676',
                            fill: false
                        }]
                    },
                    options: {
                        responsive: false,
                        title: {
                            display: true,
                            text: description,
                            position: 'top',
                            fontSize: 16,
                            fontColor: '#111',
                            padding: 20
                        },
                        scales: {
                            xAxes: [{
                                display: true,
                            }],
                            yAxes: [{
                                display: true,
                                
                            }]
                        },
                        legend: {
                            display: false,
                            position: 'top',
                            //fullSize: true,
                            fontSize: 50,
                            labels: {
                                boxWidth: 20,
                                fontColor: '#111',
                                padding: 15
                            }
                        },
                        tooltips: {
                            enabled: false
                        },
                        plugins: {
                            datalabels: {
                                color: '#111',
                                textAlign: 'center',
                                font: {
                                    lineHeight: 1
                                },
                                formatter: function(value, ctx) {
                                    return ctx.chart.data.labels[ctx.dataIndex] + '\n' + value + '%';
                                }
                            }
                        }
                    }
                })
                
        }
    }
}
</script>