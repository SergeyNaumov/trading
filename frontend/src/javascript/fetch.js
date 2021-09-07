import {config} from '/src/config'

export function httpGET(opt){
  
  fetch(config.baseURL+opt.url)
    .then((response) => {
      response=response.json()
      return response
      
    })
  .then((data) => {
      
      if(data.success){
        
        if('success' in opt){
          
          if(typeof(opt.success) == 'function' ){
            opt.success(data.data)
          }
          else{
            for(let i in data.data){
              opt.success[i]=data[i]
            }
            
          }
        }
      }
  });
}

