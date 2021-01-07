var client = require("./mysql").mysql_pool;
var mongo = require('./mongo.js');
var util = require('util')

exports.survey = function(req,res,next){
  var data = req.body;
  var bmi = req.body.con_weight/(req.body.con_stature*req.body.con_stature);
  console.log(req.body);

  client.query('select * from p_s_mbrdata where email = ?',[req.body.email],function(err, result){
      if(err){    //db연결오류
         res.json({code:500})
         console.log(err)
      }else{      //게시판 부르기성공
        var survey_mbr = result[0].memberuid;
	delete data.email;
           if(!(data.con_age && data.con_gender && data.con_stature && data.con_weight && data.h_meal && data.h_menu && data.h_nightmeal && data.h_water && data.h_drink && data.h_smoke &&
                 data.h_exercise && data.h_sleep && data.h_stress)){
              res.json({code:410})
              console.log('insert failed.(Something Empty)')
            }else{      //내용오류
                var bmi = parseInt(req.body.con_weight/((req.body.con_stature/100)*(req.body.con_stature/100)));
                data.con_bmi = bmi;
                mongo.connect(function(err){
                  if(err) throw err;
		  var date = new Date();
		  date.setHours(date.getHours()+9);
                  mongo.db.collection('survey').insert({survey_mbr:survey_mbr, survey_data:data, survey_date:date},function(err,doc){
                    if(err){
                      res.json({code:500});
                      console.log(err);
                    }else{
                      console.log('insert success')    //쓰기성공
                      res.json({code:210})
                    }
                  })
                })
            }
      }
  })

  
  if(data.eye_cataract || data.eye_glaucoma || data.eye_dry || data.eye_presbyopia || data.eye_myopia || data.eye_hyperopia || data.eye_astigmatism || data.eye_strabismus){
    data.have_eye = true;
  }
  if(data.ear_tinnitus || data.ear_tympanitis || data.ear_impairment){
    data.have_ear = true;
  }
  if(data.r_obstructive || data.r_tuberculosis || data.r_cough || data.r_asthma || data.r_pneumonia || data.r_rhinitis){
    data.have_respiratory = true;
  }
  if(data.skin_allergy || data.skin_alopecia || data.skin_cancer || data.skin_acne || data.skin_atopic || data.skin_vitiligo || data.skin_psoriasis){
    data.have_skin = true;
  }
  if(data.ger_hypertension || data.ger_diabetes){
    data.have_geriatric = true;
  }
  if(max_blood){
    var max_blood = data.max_blood
    data.max_blood = max_blood;
  }
  if(min_blood){
    var min_blood = data.min_blood
    data.min_blood = min_blood;
  }
  if(data.can_liver || data.can_stomach || data.can_lung || data.can_thyroidGland || data.can_breast || data.can_other){
    data.have_cancer = true;
  }
  if(data.fam_stroke || data.fam_myocardialInfarction || data.fam_hypertension || data.fam_diabetes || data.fam_cancer){
    data.have_family = true;
  }

  if(data.eye_cataract){
    data.eye_cataract = true;
  }
  if(data.eye_glaucoma){
    data.eye_glaucoma = true;
  }
  if(data.eye_dry){
    data.eye_dry = true;
  }
  if(data.eye_presbyopia){
    data.eye_presbyopia = true;
  }
  if(data.eye_myopia){
    data.eye_myopia = true;
  }
  if(data.eye_hyperopia){
    data.eye_hyperopia = true;
  }
  if(data.eye_astigmatism){
    data.eye_astigmatism = true;
  }
  if(data.eye_strabismus){
    data.eye_strabismus = true;
  }
  if(data.ear_tinnitus){
    data.ear_tinnitus = true;
  }
  if(data.ear_tympanitis){
    data.ear_tympanitis = true;
  }
  if(data.ear_impairment){
    data.ear_impairment = true;
  }
  if(data.r_obstructive){
    data.r_obstructive = true;
  }
  if(data.r_tuberculosis){
    data.r_tuberculosis = true;
  }
  if(data.r_cough){
    data.r_cough = true;
  }
  if(data.r_asthma){
    data.r_asthma = true;
  }
  if(data.r_pneumonia){
    data.r_pneumonia = true;
  }
  if(data.r_rhinitis){
    data.r_rhinitis = true;
  }
  if(data.skin_allergy){
    data.skin_allergy = true;
  }
  if(data.skin_alopecia){
    data.skin_alopecia = true;
  }
  if(data.skin_cancer){
    data.skin_cancer = true;
  }
  if(data.skin_acne){
    data.skin_acne = true;
  }
  if(data.skin_atopic){
    data.skin_atopic = true;
  }
  if(data.skin_vitiligo){
    data.skin_vitiligo = true;
  }
  if(data.skin_psoriasis){
    data.skin_psoriasis = true;
  }
  if(data.ger_hypertension){
    data.ger_hypertension = true;
  }
  if(data.ger_diabetes){
    data.ger_diabetes = true;
  }
  if(data.can_liver){
    data.can_liver = true;
  }
  if(data.can_stomach){
    data.can_stomach = true;
  }
  if(data.can_lung){
    data.can_lung = true;
  }
  if(data.can_thyroidGland){
    data.can_thyroidGland = true;
  }
  if(data.can_breast){
    data.can_breast = true;
  }
  if(data.can_other){
    data.can_other = true;
  }
  if(data.fam_stroke){
    data.fam_stroke = true;
  }
  if(data.fam_myocardialInfarction){
    data.fam_myocardialInfarction = true;
  }
  if(data.fam_hypertension){
    data.fam_hypertension = true;
  }
  if(data.fam_diabetes){
    data.fam_diabetes = true;
  }
  if(data.fam_cancer){
    data.fam_cancer = true;
  }
}
