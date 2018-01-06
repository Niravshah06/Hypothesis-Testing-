class Bean(object):
    def __init__(self, RANDID ,   SEX,    TOTCHOL,    AGE,    SYSBP,    DIABP,
                     CURSMOKE,    CIGPDAY,    BMI,    DIAB,    PREVCHD,    PREVAP,    PREVMI,
                         PREVSTRK,    PREVHYP,    TIME,    PERIOD,    HDLC,    LDLC,    DEATH,    ANGINA,
                             HOSPMI,    MI_FCHD ,   ANYCHD,    STROKE,    CVD,    HYPERTEN,    TIMEAP,    TIMEMI,
                                 TIMEMIFC,    TIMECHD,    TIMESTRK,    TIMECVD ,   TIMEDTH,    TIMEHYP


                 ):
        self.RANDID = RANDID
        self.SEX = SEX
        self.TOTCHOL=TOTCHOL
        self.AGE=AGE
        self.SYSBP=SYSBP
        self.DIABP=DIABP
        self.CURSMOKE=CURSMOKE
        self.CIGPDAY=CIGPDAY
        self.BMI=BMI
        self.DIAB = DIAB
        self.PREVCHD = PREVCHD
        self.PREVAP=PREVAP
        self.PREVMI=PREVMI
        self.PREVSTRK=PREVSTRK
        self.PREVHYP=PREVHYP
        self.TIME=TIME
        self.PERIOD=PERIOD
        self.HDLC=HDLC
        self.LDLC=LDLC
        self.DEATH=DEATH
        self.ANGINA=ANGINA
        self.CVD=CVD
        
        
        
        
        
        
       
        
        
    def __str__(self):
        return("Bean object:\n"
               "  id = {0}\n"
               "  Name = {1}\n"
               .format(self.RANDID, self.HDLC))
