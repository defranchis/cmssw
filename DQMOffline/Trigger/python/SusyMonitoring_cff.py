import FWCore.ParameterSet.Config as cms


from DQMOffline.Trigger.SusyMonitor_cfi import hltSUSYmonitoring



#This is added by Pablo in order to monitor the auxiliary paths for electron fake rate calculation
susyEle8CaloJet30_jet = hltSUSYmonitoring.clone()
susyEle8CaloJet30_jet.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/JetMonitor')
susyEle8CaloJet30_jet.nmuons = cms.uint32(0)
susyEle8CaloJet30_jet.nelectrons = cms.uint32(1)
susyEle8CaloJet30_jet.njets = cms.uint32(1)
susyEle8CaloJet30_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.4')
susyEle8CaloJet30_jet.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle8CaloJet30_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle8CaloJet30_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle8CaloJet30_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle8CaloJet30_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
susyEle8CaloJet30_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle8CaloJet30_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle8CaloJet30_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
susyEle8CaloJet30_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*')

susyEle8CaloJet30_ele = hltSUSYmonitoring.clone()
susyEle8CaloJet30_ele.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/ElectronMonitor')
susyEle8CaloJet30_ele.nmuons = cms.uint32(0)
susyEle8CaloJet30_ele.nelectrons = cms.uint32(1)
susyEle8CaloJet30_ele.njets = cms.uint32(1)
susyEle8CaloJet30_ele.eleSelection = cms.string('pt>10 & abs(eta)<2.4')
susyEle8CaloJet30_ele.jetSelection = cms.string('pt>80 & abs(eta)<2.4')
susyEle8CaloJet30_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle8CaloJet30_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle8CaloJet30_ele.histoPSet.elePtBinning = cms.vdouble(0,10,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle8CaloJet30_ele.histoPSet.elePtBinning2D = cms.vdouble(0,10,25,30,40,50,60,80,100,200,400)
susyEle8CaloJet30_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle8CaloJet30_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
susyEle8CaloJet30_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
susyEle8CaloJet30_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

susyEle8CaloJet30_all = hltSUSYmonitoring.clone()
susyEle8CaloJet30_all.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/GlobalMonitor')
susyEle8CaloJet30_all.nmuons = cms.uint32(0)
susyEle8CaloJet30_all.nelectrons = cms.uint32(1)
susyEle8CaloJet30_all.njets = cms.uint32(1)
susyEle8CaloJet30_all.eleSelection = cms.string('pt>10 & abs(eta)<2.4')
susyEle8CaloJet30_all.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle8CaloJet30_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle8CaloJet30_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle8CaloJet30_all.histoPSet.elePtBinning = cms.vdouble(0,10,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle8CaloJet30_all.histoPSet.elePtBinning2D = cms.vdouble(0,10,25,30,40,50,60,80,100,200,400)
susyEle8CaloJet30_all.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle8CaloJet30_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle8CaloJet30_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
# susyEle8CaloJet30_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')


susyEle8CaloIdMJet30_jet = hltSUSYmonitoring.clone()
susyEle8CaloIdMJet30_jet.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/JetMonitor')
susyEle8CaloIdMJet30_jet.nmuons = cms.uint32(0)
susyEle8CaloIdMJet30_jet.nelectrons = cms.uint32(1)
susyEle8CaloIdMJet30_jet.njets = cms.uint32(1)
susyEle8CaloIdMJet30_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.4')
susyEle8CaloIdMJet30_jet.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle8CaloIdMJet30_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle8CaloIdMJet30_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle8CaloIdMJet30_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle8CaloIdMJet30_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
susyEle8CaloIdMJet30_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle8CaloIdMJet30_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle8CaloIdMJet30_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*')
susyEle8CaloIdMJet30_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*')

susyEle8CaloIdMJet30_ele = hltSUSYmonitoring.clone()
susyEle8CaloIdMJet30_ele.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/ElectronMonitor')
susyEle8CaloIdMJet30_ele.nmuons = cms.uint32(0)
susyEle8CaloIdMJet30_ele.nelectrons = cms.uint32(1)
susyEle8CaloIdMJet30_ele.njets = cms.uint32(1)
susyEle8CaloIdMJet30_ele.eleSelection = cms.string('pt>10 & abs(eta)<2.4')
susyEle8CaloIdMJet30_ele.jetSelection = cms.string('pt>80 & abs(eta)<2.4')
susyEle8CaloIdMJet30_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle8CaloIdMJet30_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle8CaloIdMJet30_ele.histoPSet.elePtBinning = cms.vdouble(0,10,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle8CaloIdMJet30_ele.histoPSet.elePtBinning2D = cms.vdouble(0,10,25,30,40,50,60,80,100,200,400)
susyEle8CaloIdMJet30_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle8CaloIdMJet30_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
susyEle8CaloIdMJet30_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*')
susyEle8CaloIdMJet30_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

susyEle8CaloIdMJet30_all = hltSUSYmonitoring.clone()
susyEle8CaloIdMJet30_all.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/GlobalMonitor')
susyEle8CaloIdMJet30_all.nmuons = cms.uint32(0)
susyEle8CaloIdMJet30_all.nelectrons = cms.uint32(1)
susyEle8CaloIdMJet30_all.njets = cms.uint32(1)
susyEle8CaloIdMJet30_all.eleSelection = cms.string('pt>10 & abs(eta)<2.4')
susyEle8CaloIdMJet30_all.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle8CaloIdMJet30_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle8CaloIdMJet30_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle8CaloIdMJet30_all.histoPSet.elePtBinning = cms.vdouble(0,10,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle8CaloIdMJet30_all.histoPSet.elePtBinning2D = cms.vdouble(0,10,25,30,40,50,60,80,100,200,400)
susyEle8CaloIdMJet30_all.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle8CaloIdMJet30_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle8CaloIdMJet30_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*')
# susyEle8CaloIdMJet30_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')


susyEle12CaloJet30_jet = hltSUSYmonitoring.clone()
susyEle12CaloJet30_jet.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/JetMonitor')
susyEle12CaloJet30_jet.nmuons = cms.uint32(0)
susyEle12CaloJet30_jet.nelectrons = cms.uint32(1)
susyEle12CaloJet30_jet.njets = cms.uint32(1)
susyEle12CaloJet30_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.4')
susyEle12CaloJet30_jet.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle12CaloJet30_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle12CaloJet30_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle12CaloJet30_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle12CaloJet30_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
susyEle12CaloJet30_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle12CaloJet30_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle12CaloJet30_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
susyEle12CaloJet30_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*')

susyEle12CaloJet30_ele = hltSUSYmonitoring.clone()
susyEle12CaloJet30_ele.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/ElectronMonitor')
susyEle12CaloJet30_ele.nmuons = cms.uint32(0)
susyEle12CaloJet30_ele.nelectrons = cms.uint32(1)
susyEle12CaloJet30_ele.njets = cms.uint32(1)
susyEle12CaloJet30_ele.eleSelection = cms.string('pt>14 & abs(eta)<2.4')
susyEle12CaloJet30_ele.jetSelection = cms.string('pt>80 & abs(eta)<2.4')
susyEle12CaloJet30_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle12CaloJet30_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle12CaloJet30_ele.histoPSet.elePtBinning = cms.vdouble(0,12,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle12CaloJet30_ele.histoPSet.elePtBinning2D = cms.vdouble(0,12,25,30,40,50,60,80,100,200,400)
susyEle12CaloJet30_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle12CaloJet30_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
susyEle12CaloJet30_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
susyEle12CaloJet30_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

susyEle12CaloJet30_all = hltSUSYmonitoring.clone()
susyEle12CaloJet30_all.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/GlobalMonitor')
susyEle12CaloJet30_all.nmuons = cms.uint32(0)
susyEle12CaloJet30_all.nelectrons = cms.uint32(1)
susyEle12CaloJet30_all.njets = cms.uint32(1)
susyEle12CaloJet30_all.eleSelection = cms.string('pt>14 & abs(eta)<2.4')
susyEle12CaloJet30_all.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle12CaloJet30_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle12CaloJet30_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle12CaloJet30_all.histoPSet.elePtBinning = cms.vdouble(0,12,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle12CaloJet30_all.histoPSet.elePtBinning2D = cms.vdouble(0,12,25,30,40,50,60,80,100,200,400)
susyEle12CaloJet30_all.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle12CaloJet30_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle12CaloJet30_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
# susyEle12CaloJet30_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')


susyEle17CaloIdMJet30_jet = hltSUSYmonitoring.clone()
susyEle17CaloIdMJet30_jet.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/JetMonitor')
susyEle17CaloIdMJet30_jet.nmuons = cms.uint32(0)
susyEle17CaloIdMJet30_jet.nelectrons = cms.uint32(1)
susyEle17CaloIdMJet30_jet.njets = cms.uint32(1)
susyEle17CaloIdMJet30_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.4')
susyEle17CaloIdMJet30_jet.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle17CaloIdMJet30_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle17CaloIdMJet30_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle17CaloIdMJet30_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle17CaloIdMJet30_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
susyEle17CaloIdMJet30_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle17CaloIdMJet30_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle17CaloIdMJet30_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*')
susyEle17CaloIdMJet30_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*')

susyEle17CaloIdMJet30_ele = hltSUSYmonitoring.clone()
susyEle17CaloIdMJet30_ele.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/ElectronMonitor')
susyEle17CaloIdMJet30_ele.nmuons = cms.uint32(0)
susyEle17CaloIdMJet30_ele.nelectrons = cms.uint32(1)
susyEle17CaloIdMJet30_ele.njets = cms.uint32(1)
susyEle17CaloIdMJet30_ele.eleSelection = cms.string('pt>19 & abs(eta)<2.4')
susyEle17CaloIdMJet30_ele.jetSelection = cms.string('pt>80 & abs(eta)<2.4')
susyEle17CaloIdMJet30_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle17CaloIdMJet30_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle17CaloIdMJet30_ele.histoPSet.elePtBinning = cms.vdouble(0,19,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle17CaloIdMJet30_ele.histoPSet.elePtBinning2D = cms.vdouble(0,19,25,30,40,50,60,80,100,200,400)
susyEle17CaloIdMJet30_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle17CaloIdMJet30_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
susyEle17CaloIdMJet30_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*')
susyEle17CaloIdMJet30_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

susyEle17CaloIdMJet30_all = hltSUSYmonitoring.clone()
susyEle17CaloIdMJet30_all.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/GlobalMonitor')
susyEle17CaloIdMJet30_all.nmuons = cms.uint32(0)
susyEle17CaloIdMJet30_all.nelectrons = cms.uint32(1)
susyEle17CaloIdMJet30_all.njets = cms.uint32(1)
susyEle17CaloIdMJet30_all.eleSelection = cms.string('pt>19 & abs(eta)<2.4')
susyEle17CaloIdMJet30_all.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle17CaloIdMJet30_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle17CaloIdMJet30_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle17CaloIdMJet30_all.histoPSet.elePtBinning = cms.vdouble(0,19,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle17CaloIdMJet30_all.histoPSet.elePtBinning2D = cms.vdouble(0,19,25,30,40,50,60,80,100,200,400)
susyEle17CaloIdMJet30_all.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle17CaloIdMJet30_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle17CaloIdMJet30_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*')
# susyEle17CaloIdMJet30_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')


susyEle23CaloJet30_jet = hltSUSYmonitoring.clone()
susyEle23CaloJet30_jet.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/JetMonitor')
susyEle23CaloJet30_jet.nmuons = cms.uint32(0)
susyEle23CaloJet30_jet.nelectrons = cms.uint32(1)
susyEle23CaloJet30_jet.njets = cms.uint32(1)
susyEle23CaloJet30_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.4')
susyEle23CaloJet30_jet.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle23CaloJet30_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle23CaloJet30_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle23CaloJet30_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle23CaloJet30_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
susyEle23CaloJet30_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle23CaloJet30_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle23CaloJet30_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
susyEle23CaloJet30_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*')

susyEle23CaloJet30_ele = hltSUSYmonitoring.clone()
susyEle23CaloJet30_ele.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/ElectronMonitor')
susyEle23CaloJet30_ele.nmuons = cms.uint32(0)
susyEle23CaloJet30_ele.nelectrons = cms.uint32(1)
susyEle23CaloJet30_ele.njets = cms.uint32(1)
susyEle23CaloJet30_ele.eleSelection = cms.string('pt>25 & abs(eta)<2.4')
susyEle23CaloJet30_ele.jetSelection = cms.string('pt>80 & abs(eta)<2.4')
susyEle23CaloJet30_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle23CaloJet30_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle23CaloJet30_ele.histoPSet.elePtBinning = cms.vdouble(0,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle23CaloJet30_ele.histoPSet.elePtBinning2D = cms.vdouble(0,25,30,40,50,60,80,100,200,400)
susyEle23CaloJet30_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle23CaloJet30_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
susyEle23CaloJet30_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
susyEle23CaloJet30_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

susyEle23CaloJet30_all = hltSUSYmonitoring.clone()
susyEle23CaloJet30_all.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/GlobalMonitor')
susyEle23CaloJet30_all.nmuons = cms.uint32(0)
susyEle23CaloJet30_all.nelectrons = cms.uint32(1)
susyEle23CaloJet30_all.njets = cms.uint32(1)
susyEle23CaloJet30_all.eleSelection = cms.string('pt>14 & abs(eta)<2.4')
susyEle23CaloJet30_all.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle23CaloJet30_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle23CaloJet30_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle23CaloJet30_all.histoPSet.elePtBinning = cms.vdouble(0,12,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle23CaloJet30_all.histoPSet.elePtBinning2D = cms.vdouble(0,12,25,30,40,50,60,80,100,200,400)
susyEle23CaloJet30_all.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle23CaloJet30_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle23CaloJet30_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v*')
# susyEle23CaloJet30_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')

susyEle23CaloIdMJet30_jet = hltSUSYmonitoring.clone()
susyEle23CaloIdMJet30_jet.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/JetMonitor')
susyEle23CaloIdMJet30_jet.nmuons = cms.uint32(0)
susyEle23CaloIdMJet30_jet.nelectrons = cms.uint32(1)
susyEle23CaloIdMJet30_jet.njets = cms.uint32(1)
susyEle23CaloIdMJet30_jet.eleSelection = cms.string('pt>50 & abs(eta)<2.4')
susyEle23CaloIdMJet30_jet.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle23CaloIdMJet30_jet.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle23CaloIdMJet30_jet.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle23CaloIdMJet30_jet.histoPSet.elePtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle23CaloIdMJet30_jet.histoPSet.elePtBinning2D = cms.vdouble(0,50,70,120,200,400)
susyEle23CaloIdMJet30_jet.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle23CaloIdMJet30_jet.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle23CaloIdMJet30_jet.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*')
susyEle23CaloIdMJet30_jet.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*')

susyEle23CaloIdMJet30_ele = hltSUSYmonitoring.clone()
susyEle23CaloIdMJet30_ele.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/ElectronMonitor')
susyEle23CaloIdMJet30_ele.nmuons = cms.uint32(0)
susyEle23CaloIdMJet30_ele.nelectrons = cms.uint32(1)
susyEle23CaloIdMJet30_ele.njets = cms.uint32(1)
susyEle23CaloIdMJet30_ele.eleSelection = cms.string('pt>25 & abs(eta)<2.4')
susyEle23CaloIdMJet30_ele.jetSelection = cms.string('pt>80 & abs(eta)<2.4')
susyEle23CaloIdMJet30_ele.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle23CaloIdMJet30_ele.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle23CaloIdMJet30_ele.histoPSet.elePtBinning = cms.vdouble(0,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle23CaloIdMJet30_ele.histoPSet.elePtBinning2D = cms.vdouble(0,25,30,40,50,60,80,100,200,400)
susyEle23CaloIdMJet30_ele.histoPSet.jetPtBinning = cms.vdouble(0,50,60,80,120,200,400)
susyEle23CaloIdMJet30_ele.histoPSet.jetPtBinning2D = cms.vdouble(0,50,60,80,100,200,400)
susyEle23CaloIdMJet30_ele.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*')
susyEle23CaloIdMJet30_ele.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_PFJet60_v*')

susyEle23CaloIdMJet30_all = hltSUSYmonitoring.clone()
susyEle23CaloIdMJet30_all.FolderName = cms.string('HLT/SusyHLTOffline/SusyMonitor/EleJet/GlobalMonitor')
susyEle23CaloIdMJet30_all.nmuons = cms.uint32(0)
susyEle23CaloIdMJet30_all.nelectrons = cms.uint32(1)
susyEle23CaloIdMJet30_all.njets = cms.uint32(1)
susyEle23CaloIdMJet30_all.eleSelection = cms.string('pt>14 & abs(eta)<2.4')
susyEle23CaloIdMJet30_all.jetSelection = cms.string('pt>35 & abs(eta)<2.4')
susyEle23CaloIdMJet30_all.histoPSet.eleEtaBinning = cms.vdouble(-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1)
susyEle23CaloIdMJet30_all.histoPSet.eleEtaBinning2D = cms.vdouble(-2.1,-1.5,-0.6,0,0.6,1.5,2.1)
susyEle23CaloIdMJet30_all.histoPSet.elePtBinning = cms.vdouble(0,12,25,30,32.5,35,40,45,50,60,80,120,200,400)
susyEle23CaloIdMJet30_all.histoPSet.elePtBinning2D = cms.vdouble(0,12,25,30,40,50,60,80,100,200,400)
susyEle23CaloIdMJet30_all.histoPSet.jetPtBinning = cms.vdouble(0,30,35,37.5,40,50,60,80,120,200,400)
susyEle23CaloIdMJet30_all.histoPSet.jetPtBinning2D = cms.vdouble(0,30,35,40,50,60,80,100,200,400)
susyEle23CaloIdMJet30_all.numGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*')
# susyEle23CaloIdMJet30_all.denGenericTriggerEventPSet.hltPaths = cms.vstring('HLT_IsoMu24_v*')

 




susyMonitorHLT = cms.Sequence(
    susyEle8CaloJet30_ele
    + susyEle8CaloJet30_jet
    + susyEle8CaloJet30_all
    + susyEle12CaloJet30_ele
    + susyEle12CaloJet30_jet
    + susyEle12CaloJet30_all
    + susyEle23CaloJet30_ele
    + susyEle23CaloJet30_jet
    + susyEle23CaloJet30_all
    + susyEle8CaloIdMJet30_ele
    + susyEle8CaloIdMJet30_jet
    + susyEle8CaloIdMJet30_all
    + susyEle17CaloIdMJet30_ele
    + susyEle17CaloIdMJet30_jet
    + susyEle17CaloIdMJet30_all
    + susyEle23CaloIdMJet30_ele
    + susyEle23CaloIdMJet30_jet
    + susyEle23CaloIdMJet30_all
    )
