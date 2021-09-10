// проверяет, подошла ли компания по 
export function search_param_ok(c, SF){
  
  let sf_header=SF.header.toLowerCase()

  let ok=true
  if(sf_header && !c.header.toLowerCase().includes(sf_header) && !c.sticker.toLowerCase().includes(SF.header) ){
    ok=false
  }
  
  // числовые фильтры
  let digit_filters=['pe','ps','pb', 'roe', 'roa', 'roi'] // 
  for(let f of digit_filters){
    
    if(SF[f][0]!=false){
      
      if(c[f]<SF[f][0]){
        
        return false
      }
    }
    
    if(SF[f][1]!=false){
      
      if(c[f] > SF[f][1]){
        
        return false
      }
    }    
  }
  
  return ok
}

export function dynamic_style(name,v){
  if(name=='pe' && (v<0 || v>20) ) {
      return {'font-weight':'bold',color:'red'}
  }
  if(name=='div_payout_ratio' && (v>50) && (v<70) ){
      return {color:'rgb(181 26 0)'}
  }
  if(name=='div_payout_ratio' && (v>70) ){
      return {'font-weight':'bold',color:'red'}
  }
  if(name=='div_payout_ratio' && (v>8) ){
      return {'font-weight':'bold',color:'green'}
  }
  if(name=='debt_ebitda'){
    if(v<0.2){
      return {color:'green'}
    }
    else if(v>0.5 && v<1){
      return {color:'orange','font-weight':'bold'}
    }
    else if(v>=1){
      return {color:'red','font-weight':'bold'}
    }
  }
  return ''
}