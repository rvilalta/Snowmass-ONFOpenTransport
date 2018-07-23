# Change Log
## Commit Range: v1.0.3..v2.0.0


* __Update README with changed links/pointers after the ONF &amp; ON.Lab merger__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Jan 2018 17:26:00 -0500
    [109e7f2e313e6b54f157532ba1eed1c7b6d308cd](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/109e7f2e313e6b54f157532ba1eed1c7b6d308cd) 
    

* __Change Log since release version 1.0.3 in markdown format__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Jan 2018 17:11:01 -0500
    [42553d58759baebe250403dc00a15fb4cff707b6](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/42553d58759baebe250403dc00a15fb4cff707b6) 
    

* __Change log since release version 1.0.3__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 3 Jan 2018 16:39:14 -0500
    [d99e6191837f01e84f4a9b0e50dc39b7b36bdd76](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d99e6191837f01e84f4a9b0e50dc39b7b36bdd76) 
    

* __Fix Issue #259: Fixed descriptions for NotificationType &amp; ObjectType__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 2 Jan 2018 15:50:54 -0500
    [c7594711ce0f995b91ca6ed91a30f7615d368820](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c7594711ce0f995b91ca6ed91a30f7615d368820) 
    

* __Fixes for Issues #262, #265, #266, #267, #271, #272, #273, #276__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 2 Jan 2018 15:37:39 -0500
    [cbecb7f6190b598e5ff44fbf035fe301ec47cb59](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/cbecb7f6190b598e5ff44fbf035fe301ec47cb59) 
    - #262: Update the UML model attribute *layerProtocolName* with the UML
    *\&lt;\&lt;Preliminary\&gt;\&gt;* stereotype
    - #265: Update the UML model Enum/Datatype *LifecycleState* with the UML
    *\&lt;\&lt;Preliminary\&gt;\&gt;* stereotype
    - #265: Replace *LifeCycle* Enum/Data value *POTENTIAL* with
    *POTENTIAL_AVAILABLE* and *POTENTIAL_BUSY* values (discussed previously in the
    F2F meeting)
    - #266: Update the UML model Enum/Datatype/Pac and related attributes for
    *TerminationDirection* with the UML *\&lt;\&lt;Experimental\&gt;\&gt;* stereotype
    - #272: Update the UML model Enum/Datatype/Pac and related attributes for
    *TerminationState* with the UML *\&lt;\&lt;Experimental\&gt;\&gt;* stereotype
    - #271: Update the UML model Enum/Datatype *DirectiveValue* with the UML
    *\&lt;\&lt;Experimental\&gt;\&gt;* stereotype
    - #273: Update the UML model Enum/Datatype *CapacityUnit* with additional
    enumeration value *TBPS*
    - #276: Update the UML model Enum/Datatype *CapacityUnit* with additional
    enumeration values *TB, GB, MB, KB* that represent the raw-byte-size unit.
    - #267: Update the UML model Enum/Datatype *LayerprotocolName* with additional
    enumeration value *OCH*
    
    

* __Changes to yang, tree &amp; swagger files due to model optimization updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 5 Dec 2017 17:15:24 -0500
    [d221399fe4e96d9e2b0a7ebe79027a001e3cc85c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d221399fe4e96d9e2b0a7ebe79027a001e3cc85c) 
    

* __UML Diagram updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 5 Dec 2017 17:07:49 -0500
    [c94d740b6f1a0dd20abd4cd768f2fecb7f13d29c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c94d740b6f1a0dd20abd4cd768f2fecb7f13d29c) 
    

* __Model Optimization &amp; Renaming: Removed redundant associations__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 5 Dec 2017 16:54:02 -0500
    [d6e6b876f14678825779a5dade4d02e894464789](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d6e6b876f14678825779a5dade4d02e894464789) 
    - Renamed association CEPHasClientNEP to CEPSupportsClientNEP
    - Renamed association CEPHasServerNEP to CEPIsSupportedByNEP and its 
    association-end ConnectionEndPoint:_serverNodeEdgePoint to 
    ConnectionEndPoint:_parentNodeEdgePoint
    - Renamed CSEPHasCEP to CEPRelatesToCSEP and reversed navigation direction
    - Removed association: CEPConnectsToPeerCEP
    - Removed association: ConnectionSupportsLink
    - Removed association: ConnectionIsBoundedByNode

* __Optimization: Removed association-LinkHasAsociatedNodes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 5 Dec 2017 15:43:07 -0500
    [3dcb4b9bd7a6e8d15ccdc726bde2ebb9e021e2a2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/3dcb4b9bd7a6e8d15ccdc726bde2ebb9e021e2a2) 
    

* __Changes due to Eagle Uml2Yang tool update to handle &lt;ExtendedComposite&gt;__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Nov 2017 15:45:00 -0500
    [92d503a7388b2d87e1e61d4727c841c5802385a4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/92d503a7388b2d87e1e61d4727c841c5802385a4) 
    - the previous versions of the Uml2Yang tool was treating
    &lt;ExtendedComposite&gt; same as &lt;StrictComposite&gt; by generating container/list
    statement. Now the tool generates &#34;uses&#34; statement for
    &lt;ExtendedComposite&gt; without the enclosing container/list statement.

* __Temp Fix: Made OTSi Pac attributes read-only to avoid defining keys for data-types__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Nov 2017 15:40:50 -0500
    [7e19e92ae972b0a3a37ad3d0083cf8e4c480ed1e](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7e19e92ae972b0a3a37ad3d0083cf8e4c480ed1e) 
    

* __Bug Fix: Corrected stereotypes to &lt;ExtendedComposite&gt;__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Nov 2017 15:18:22 -0500
    [c098a6dd11857bec855b620c4da8c9a278e07fb5](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c098a6dd11857bec855b620c4da8c9a278e07fb5) 
    - The topologyConstraint, connectivityConstraint &amp; resilienceConstraint in
    ConnectivityService were incorrectly annotated as &lt;StrictComposite&gt; instead of
    &lt;ExtendedComposite&gt;
    - The Ethernet Spec model pac associations were not annotated with
    &lt;ExtendedComposite&gt; stereotypes

* __Changes due to Eagle Uml2Yang tool updates to preserve UML literal names__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 20 Nov 2017 09:43:04 -0500
    [ff9cb9020383d060e0884be0e8b4ee20bbfee81c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ff9cb9020383d060e0884be0e8b4ee20bbfee81c) 
    - the Eagle Uml2Yang tool was updated to preserve the literal names as defined
    in UML model. Since TAPI UML uses &#34;ALL_CAPS&#34; for enumeration literals, the
    resulting yang enums are now named in &#34;ALL_CAPS&#34;

* __Bug fix: ContextHasPathCompService should be &lt;StrictComposite&gt;__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Sun, 19 Nov 2017 15:05:51 -0500
    [1dbc14f0d2f2f2186b3a22d195234143bcab4ccb](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/1dbc14f0d2f2f2186b3a22d195234143bcab4ccb) 
    

* __Bug Fix: Changed all TAPI Enumerations to non-extensible (isLeaf=true)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 17 Nov 2017 08:42:21 -0500
    [e5eacd7d7889cbb097f5505f18140fd378e3ebf2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e5eacd7d7889cbb097f5505f18140fd378e3ebf2) 
    The Papyrus default isLeaf=false due to whcih some of the enums were 
    unintentionally tagged as extensible and hence being mapped to identity

* __Changes due to folding of LayerProtocol into NEP &amp; CEP classes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 13 Nov 2017 15:26:32 -0500
    [81d1d21710cf843bd446bb8e974492bd588e03f4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/81d1d21710cf843bd446bb8e974492bd588e03f4) 
    - includes updates to ETH spec model to augment NEP &amp; CEP instead of 
    LayerProtocol

* __Split Layerprotocol class into layerProtocolName &amp; TerminationPac__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 10 Nov 2017 17:25:23 -0500
    [fa9df17fa08fe4132c9d07b323651310c258bfc3](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fa9df17fa08fe4132c9d07b323651310c258bfc3) 
    Decision made in Sept 2017 TAPI calls to augment the LTPs directly rather than
    the LayerProtocol. Also agreed to make the NEPs &amp; CEPs as single layer
    entities. These decisions allow for folding layerProtocol attributes into the
    LTPs (ExtendedCOmposite rather than StrictComposite). The advantage in having
    the layerProtocolName as an LTP attribute allows for simple conditional
    specification/augment.   

* __Added OduPmPac &amp; OduDecfectPac__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 8 Sep 2017 13:26:31 -0400
    [d877528dd331b655f4dd20a1816505a1b23886bd](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d877528dd331b655f4dd20a1816505a1b23886bd) 
    

* __Fixes &amp; typos to initial version from review during 09/05 call__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 8 Sep 2017 00:49:48 -0400
    [bed4a487a4b610d0ae1bd54029aec497c17e1960](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/bed4a487a4b610d0ae1bd54029aec497c17e1960) 
    

* __Updated ODU OAM model with TCM &amp; NCM MEP attributes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 8 Sep 2017 00:21:25 -0400
    [42f94dab52437ff65be7f76e84e00578b71f917f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/42f94dab52437ff65be7f76e84e00578b71f917f) 
    

* __Yang/Swagger updates related to previous UML updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 7 Sep 2017 22:43:30 -0400
    [98f9e183b1284d0e77256625859ba04a00eaf49d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/98f9e183b1284d0e77256625859ba04a00eaf49d) 
    - Updated LayerProtocol with ETY, OTSI_A &amp; OTU.
    - Added monitoredDirection to MEP
    - resilienceType update
    - capacityType updates
    - other misc updates such as data-type keys

* __added monitoredDirection attribute to MEP__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 7 Sep 2017 22:24:27 -0400
    [025ec599bd20fb355f81c94520debc793ee5d135](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/025ec599bd20fb355f81c94520debc793ee5d135) 
    

* __Add files via upload__

    [openflow-lyo](mailto:lyong@ciena.com) - Tue, 5 Sep 2017 10:12:38 -0700
    [2140591cc91324076f36d55406474e55b12e8c15](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/2140591cc91324076f36d55406474e55b12e8c15) 
    

* __ODU Model updates - added oduProtectionPac__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 4 Sep 2017 17:22:40 -0400
    [94989aa5e2d56a51c15636b5b00173879413fc5d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/94989aa5e2d56a51c15636b5b00173879413fc5d) 
    

* __Updated LayerProtocolName to add OTSiA, OTU &amp; ETY layers__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 1 Sep 2017 09:38:57 -0400
    [81d0a8fce27234b1d90604020d2694d36848c9a4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/81d0a8fce27234b1d90604020d2694d36848c9a4) 
    

* __Initial draft of OTSi Spec - replaced OCh Spec__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 1 Sep 2017 09:37:33 -0400
    [570111b8d9c5169a24c9cca4c7abc7a08ebb71f9](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/570111b8d9c5169a24c9cca4c7abc7a08ebb71f9) 
    

* __Working on TAPI_RI for TAPI 2.0 - skeleton from swagger-codegen__

    [Ricard Vilalta](mailto:rvilalta@gmail.com) - Wed, 30 Aug 2017 04:46:10 +0100
    [bbcac4055747b75ba84b66e2dac31f6a6309ece7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/bbcac4055747b75ba84b66e2dac31f6a6309ece7) 
    

* __Minor UML association renaming__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 29 Aug 2017 17:05:27 -0400
    [af3a925510af048331a410235bfc65938149162f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/af3a925510af048331a410235bfc65938149162f) 
    

* __Renamed OduNodeEdgePointLpSpec and OduConnectionEndPointLpSpec__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 29 Aug 2017 16:53:42 -0400
    [76ed68887549e1eb62ce4257d48b7d751e3c322b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/76ed68887549e1eb62ce4257d48b7d751e3c322b) 
    to OduNodeEdgePointSpec &amp; OduConnectionEndPointSpec

* __Updated ODU Spec Model draft/skeleton as per TAP &amp; IMP discussions__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 29 Aug 2017 16:38:10 -0400
    [59168e43499cd3db9af7c3ae6f4d8f225ebafd70](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/59168e43499cd3db9af7c3ae6f4d8f225ebafd70) 
    

* __Yang/Tree/Swagger files for updated Resilience UML model (by Rod)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 24 Aug 2017 12:54:55 -0400
    [f9774d4566f59252fdc158f9fbf89ea6357e9605](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/f9774d4566f59252fdc158f9fbf89ea6357e9605) 
    

* __Add a protectionRole attribute to ConnectivityServiceEndPoint__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 17:24:22 +0800
    [6e2a75dbf33596512472f858b081603fd624e673](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/6e2a75dbf33596512472f858b081603fd624e673) 
    Add a protectionRole attribute to ConnectivityServiceEndPoint to specify the
    protection role of this Port when create or update ConnectivityService.

* __Update the TapiConnectivity Interfaces__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 17:08:07 +0800
    [fa93a0a92cb4b489d37184bbf00cf6596bb68b58](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fa93a0a92cb4b489d37184bbf00cf6596bb68b58) 
    Update the TapiConnectivity createConnectivityService and 
    updateConnectivityService with ResilienceConstraint.

* __Add RouteComputePolicy to TapiConnectivity__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 17:03:13 +0800
    [4ab965be3dc16b1aac8cc1dff05e52d2d4a69eaa](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4ab965be3dc16b1aac8cc1dff05e52d2d4a69eaa) 
    1) Create RouteComputePolicy to TapiConnectivity with routeObjectiveFunction
    and diversityPolicy attributes; 2) Create a new diagram OTSiRoutingSpec to
    TapiOCh; 3) Create OpticalRoutingSpec with opticalRoutingStrategy in TapiOCh to
    augment RouteComputePolicy.

* __Add isExclusiveService attribute to ConnectivityConstraint__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 16:16:47 +0800
    [54088c1787dfa13e7cd8ad6045e41d2603d39024](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/54088c1787dfa13e7cd8ad6045e41d2603d39024) 
    Add isExclusiveService attribute to ConnectivityConstraint to distinguish if
    the ETH service is a virtual service (i.e. between EPL(true) and EVPL(false),
    or between EPLAN(true) and EVPLAN(false) )

* __Add ResilienceConstraint to TapiConnecitivty__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 15:54:06 +0800
    [d8992ee944e8411a143e7e896c619cdc586295e5](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d8992ee944e8411a143e7e896c619cdc586295e5) 
    1) Rename the ControlParameterPac to ResilienceConstraint; 2) Modify the 
    ResilienceConstraint with the attributes per discussed in Aug.23 call. 3) Make
    the ResilienceConstraint aggregated to ConnectivityService.

* __Add the resilienceType attribute to Link object class__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 15:11:53 +0800
    [4d8f3491cb4bb9069c954fbfdd925d8a720cbb76](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4d8f3491cb4bb9069c954fbfdd925d8a720cbb76) 
    

* __add Data type - ResilienceType__

    [RodLU](mailto:lu.rongduo@zte.com.cn) - Wed, 23 Aug 2017 14:50:35 +0800
    [e5178229da85dcd0d7aaea88d38b685539a99d40](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e5178229da85dcd0d7aaea88d38b685539a99d40) 
    Add a data type ResilienceType to TapiTopology with restorationPolicy and
    protectionType attributes. Also add two enumeration types RestorationPolicy and
    ProtectionType to TapiTopology.

* __TAPI OAM model updates as per TAPI/IMP calls from 08/14 &amp; 8/17__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 17 Aug 2017 13:14:26 -0400
    [f1bbafc1422e78a43ff5519298eaed1bd03df3d1](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/f1bbafc1422e78a43ff5519298eaed1bd03df3d1) 
    - moved MEP/MIP containment to MEG, ME now aggregates MEP/MIP to allow for
    sharing of MEPs by multiple MEs in case of rooted-multipoint
    - added an association from ME to Connection Route
    - flattened MEP by removing source/sink/bi pacs and moving their attributes
    into MEP
    - added layerProtocolName attribute to MEP/MIP
    - added adminState attribute to pro-active/on-demand measurement jobs 
    

* __Minor UML-only fixes - stereotype and multiplicity of StatePac__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 16 Aug 2017 18:00:03 -0400
    [b2cc0bdf9c68b69f9a0ed3c4bee4dfc20e6938e4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b2cc0bdf9c68b69f9a0ed3c4bee4dfc20e6938e4) 
    

* __Fixes #247 - removed multiple keys for the TopologyPac datatypes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 16 Aug 2017 16:42:07 -0400
    [caff6c520d612773ce0609749b6134b433484971](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/caff6c520d612773ce0609749b6134b433484971) 
    

* __Capacity datatype fixes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 16 Aug 2017 16:07:08 -0400
    [5b6cb7cfbdfa4d9e2634adfd7e109f22304a0830](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5b6cb7cfbdfa4d9e2634adfd7e109f22304a0830) 
    - Updated comment for totalSize attribute to indicate that in case of 
    bandwidthProfile, this is expected to same as CIR
    - renamed FixedCapacityValue datatype to CapacityValue
    - made bandwidthProfile attribute as optional
    - changed the type from Integer to CapacityValue for following BandwidthProfile
    attributes: committedInformationRate, committedBustSize, peakInformationRate &amp;
    peakBurstSize
    - removed the &#34;NOT_APPLICABLE&#34; enum value for CapacityUnit and 
    BandwidthProfileTYpe enumerations

* __Add files via upload__

    [openflow-lyo](mailto:lyong@ciena.com) - Sun, 13 Aug 2017 21:06:24 -0700
    [d647f95ab5152cfd10e2e134e5a76d0e393f33b3](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d647f95ab5152cfd10e2e134e5a76d0e393f33b3) 
    

* __Swagger file updates due to Connectivity, OAM &amp; Spec model updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 7 Aug 2017 00:05:12 -0400
    [afe5bbf05a8b21c150838ed3719f109124f9df1c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/afe5bbf05a8b21c150838ed3719f109124f9df1c) 
    

* __Add files via upload__

    [openflow-lyo](mailto:lyong@ciena.com) - Thu, 3 Aug 2017 04:07:25 -0700
    [aa1fe10a658fa185184ed8c51285e03331feead4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/aa1fe10a658fa185184ed8c51285e03331feead4) 
    

* __OAM model updates as per previous TAPI and IMP discussions__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 28 Jul 2017 11:12:23 -0400
    [df1810f1c717a5cfba4a3d4498c794783b8cc566](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/df1810f1c717a5cfba4a3d4498c794783b8cc566) 
    

* __Fixes #242 &amp; #237 (partial fix - model update only)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 27 Jul 2017 16:18:06 -0400
    [25ac20bfe6e174382c9b8a82484035e243b889ae](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/25ac20bfe6e174382c9b8a82484035e243b889ae) 
    

* __Renamed ODU_2_3_SlotType enum to OduSlotType to enable proper yang__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 18 Jul 2017 16:35:18 -0400
    [9a317a27d4b9fbc1ab244f8fb75e24abb83b2796](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9a317a27d4b9fbc1ab244f8fb75e24abb83b2796) 
    

* __Renamed ODU_2_3_SlotType enum to OduSlotType to enable proper yang__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 18 Jul 2017 16:34:36 -0400
    [5ce6483213edfc066d76f2ee6c4f6c151f716953](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5ce6483213edfc066d76f2ee6c4f6c151f716953) 
    

* __Fixed typo: &#34;POINT_TO_MULTIPOINT_CONNECTIVTY&#34; -&gt; &#34;POINT_TO_MULTIPOINT_CONNECTIVITY&#34;__

    [Pedro Costa](mailto:pedro.costa.ext@coriant.com) - Thu, 13 Jul 2017 12:29:24 +0100
    [11c1b1f069950bf8b5d5af184ec9b5c891abc945](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/11c1b1f069950bf8b5d5af184ec9b5c891abc945) 
    

* __Fixed typo: &#34;exlude-node&#34; -&gt; &#34;exclude-node&#34;__

    [Pedro Costa](mailto:pedro.costa.ext@coriant.com) - Thu, 13 Jul 2017 11:59:43 +0100
    [ae7e82f4f99f7e684aeb7188d9974bbad1c03ee2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ae7e82f4f99f7e684aeb7188d9974bbad1c03ee2) 
    

* __Update tapi-connectivity.yang__

    [Pedro Costa](mailto:pedro.costa.ext@coriant.com) - Thu, 13 Jul 2017 11:41:35 +0100
    [59d00842b6d0de4a01cad0e6cd3305e09cfa58da](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/59d00842b6d0de4a01cad0e6cd3305e09cfa58da) 
    Fixed &#34;exlude-node&#34; -&gt; &#34;exclude-node&#34; typo

* __ODU Spec updated after the OTWG IM call on July 11, 2017__

    [i00279872](mailto:i00279872@DELL-LTVBAJCETN.china.huawei.com) - Wed, 12 Jul 2017 11:28:06 +0200
    [8c9bce87f76aec94fb82deac76ae79175a20917f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8c9bce87f76aec94fb82deac76ae79175a20917f) 
    

* __Updates to .yang, .tree &amp; .swagger files using latest Xmi2Yang tool__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 11 Jul 2017 15:41:55 -0400
    [aba6a96df09ad84aa791cbe642902c0d36d827d1](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/aba6a96df09ad84aa791cbe642902c0d36d827d1) 
    - the main change is reverting the addition of &#39;-g&#39; suffix to the yang 
    groupings/classes/complex-data-types
    - also includes updates to the yang, tree &amp; swagger files resulting from 
    following fixes/changes #230, #232, #234, #236

* __TAPI OAM Model updates as per IMP call on June 29__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 11 Jul 2017 08:24:58 -0400
    [b1fa562d5ccd049d8a2ff05e408b49a6af43c9da](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b1fa562d5ccd049d8a2ff05e408b49a6af43c9da) 
    

* __Added operation to updateSIP.adminState &amp; fixed ConnService operations__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 7 Jul 2017 15:10:06 -0400
    [344a2123432d9835b44f355d96146ff6d279fe8e](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/344a2123432d9835b44f355d96146ff6d279fe8e) 
    

* __Fix #233 - added AdminStatePac to CSEP and SIP__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 7 Jul 2017 14:02:52 -0400
    [d41fc7f6a68193c986c39372a7b86e7e9702da61](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d41fc7f6a68193c986c39372a7b86e7e9702da61) 
    - Also made CSEP and SIP editable/configurable to be able to set this

* __Add files via upload__

    [openflow-lyo](mailto:lyong@ciena.com) - Thu, 6 Jul 2017 16:42:00 -0700
    [23593ddbe919e7e999cf493faf676320d5671a7d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/23593ddbe919e7e999cf493faf676320d5671a7d) 
    

* __Oam Model as of IMP call on 06/29__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 5 Jul 2017 23:13:24 -0400
    [5dead2c07a3f546c26534c4db62395d0e456e892](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5dead2c07a3f546c26534c4db62395d0e456e892) 
    

* __Fix #227: Replaced FixedCapacityValue Enum with complex DataType__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 5 Jul 2017 18:24:39 -0400
    [58656909f007ab7c5da401dc4cd31195ff6e6238](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/58656909f007ab7c5da401dc4cd31195ff6e6238) 
    - FixedCapacityValue is now a complex DataType with 2 attributes - an integer
    value and an unit enumeration
    - Also refactored TimeRange Class to a complex DataType
    - Renamed UniversalId DataType to Uuid and added &lt;reference&gt; stereotype to
    RFC6991 and value for yang-import (for eagle tool)

* __Migrate TAPI to OpenModelProfile 0.2.11 OpenInterfaceModelProfile 0.0.7__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 26 Jun 2017 23:38:23 -0400
    [46678357fa5ebc142260e83bbd65d1fe0bc0cf72](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/46678357fa5ebc142260e83bbd65d1fe0bc0cf72) 
    

* __Updated the target for the OamLpSpec__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 22 Jun 2017 10:23:14 -0400
    [a9a011b6f13ceb0d5ddb3daf2e45c7c1b0a6618f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a9a011b6f13ceb0d5ddb3daf2e45c7c1b0a6618f) 
    

* __Added OamServiceSkeleton diagram as per discussion on 06/22/17 IMP call__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 22 Jun 2017 10:09:58 -0400
    [0f8a4ef6cf24459e162d1a990ac96ddaa36f9cd2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/0f8a4ef6cf24459e162d1a990ac96ddaa36f9cd2) 
    

* __Fix the old &#39;service-end-point&#39; name in ObjectType of notification module.__

    [lurongduo](mailto:10184088@zte.com.cn) - Wed, 14 Jun 2017 16:02:26 +0800
    [9986c89782cf2bf55153fa5b2129b1cd31a6298b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9986c89782cf2bf55153fa5b2129b1cd31a6298b) 
    

* __Added LayerProtocol to OamServiceEndPoint, removed Connection association from OamService__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 12 Jun 2017 03:22:15 -0400
    [1c05b2570a7d6b9f083824b9bf78885fbdca0bc9](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/1c05b2570a7d6b9f083824b9bf78885fbdca0bc9) 
    

* __minor diagram updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 12 Jun 2017 00:42:38 -0400
    [f6ab4aabc7784ce173b04e62937e4ac2bb1ca960](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/f6ab4aabc7784ce173b04e62937e4ac2bb1ca960) 
    

* __Added missing includeNode/excludeNode attributes into TopologyConstraint__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 12 Jun 2017 00:41:56 -0400
    [9195e976886a6ee15bc6ee17df42905a4e23f5da](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9195e976886a6ee15bc6ee17df42905a4e23f5da) 
    

* __Fixes #224,#225 Redefined Route as series of CEPs instead of Connections__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 8 Jun 2017 02:56:51 -0400
    [ea422f6bdc6889b791ea8857bde0277d94a6470e](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ea422f6bdc6889b791ea8857bde0277d94a6470e) 
    Also added following associations to Connection:
    - ConnectionHasLowerLevelConnections
    - ConnectionSupportsLinks

* __Fixes #199,#200,#201 Added Capacity to SIP, CSEP, LayerProtocol to CSEP__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 8 Jun 2017 01:28:52 -0400
    [a0701d895591ae0944aef43d4fbe90de8d86407e](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a0701d895591ae0944aef43d4fbe90de8d86407e) 
    - Also moved the CapacityPac and Capacity DataTypes from TapiTopology to 
    TapiCommon
    

* __Fixes #199, #200, #201__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 8 Jun 2017 01:06:23 -0400
    [3682bf310914914005fe2c184636f60c27337bb6](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/3682bf310914914005fe2c184636f60c27337bb6) 
    

* __Fix #215 - Deleted TerminationDirection from SIP, NEP &amp; CEP classes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 23:24:24 -0400
    [5a456a04a3d9abb03a35f71ad8068a43bb2a1ae5](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5a456a04a3d9abb03a35f71ad8068a43bb2a1ae5) 
    

* __Renamed ProtType to SwitchType and UML stereotype/aggregation update__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 22:18:11 -0400
    [a91a2571a828a0c33a0162b62159e56f21b1fee8](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a91a2571a828a0c33a0162b62159e56f21b1fee8) 
    

* __Minor UML stereotype correction on NodeConstraint diagram__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 22:17:04 -0400
    [fc742805af7d42df90e16e40eb3edcaf69336186](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fc742805af7d42df90e16e40eb3edcaf69336186) 
    

* __Added description noting that NEP&lt;--&gt;SIP mapping &gt; 1 as experimental__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 22:04:52 -0400
    [c2caa96aeeab5185fbebcc295beae8f72a831e21](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c2caa96aeeab5185fbebcc295beae8f72a831e21) 
    

* __Fix #191 - Removed label attribute from the TAPI GlobalClass__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 22:00:10 -0400
    [30b7b8164435e1348a7e4d16e1bd44bbcae2699c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/30b7b8164435e1348a7e4d16e1bd44bbcae2699c) 
    

* __Renamed OamLpSPec to MepMipReference (based on TAPI call discussion)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 21:55:15 -0400
    [7b66b262bcd01607ebe65dd8071517525a24612a](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7b66b262bcd01607ebe65dd8071517525a24612a) 
    

* __Fix #191 - Removed label attribute from the TAPI GlobalClass__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 21:11:19 -0400
    [e7c26016968fabf9bd693547ddb28ddd962787c7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e7c26016968fabf9bd693547ddb28ddd962787c7) 
    

* __Fix #191 - Removed label attribute from the TAPI GlobalClass__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 7 Jun 2017 21:09:15 -0400
    [aa250232eb804eb55ea500faaa2f30e0c2f24236](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/aa250232eb804eb55ea500faaa2f30e0c2f24236) 
    

* __T-API ODU Spec updated as per comments in onf2016.215.15__

    [i00279872](mailto:i00279872@DELL-LTVBAJCETN.china.huawei.com) - Fri, 2 Jun 2017 15:41:42 +0200
    [435b36a1f565c37858eb1c0e83206fcf4271392d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/435b36a1f565c37858eb1c0e83206fcf4271392d) 
    

* __Fixing broken links in README.md__

    [Yuta HIGUCHI](mailto:y-higuchi@users.noreply.github.com) - Thu, 1 Jun 2017 20:47:51 -0700
    [08e576ab06f4801fc8f771ddd2c207c9a91d57cc](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/08e576ab06f4801fc8f771ddd2c207c9a91d57cc) 
    Fixed broken links in README.md and some Markdown syntax

* __Updates to TAPI yang, tree &amp; swagger files using latest Eagle toolchain__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 31 May 2017 18:01:06 -0400
    [acff9dcf703307fd28c83e9b39d7ccbac0517eef](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/acff9dcf703307fd28c83e9b39d7ccbac0517eef) 
    - the main update is mapping extensible enumeration to identity
    - currently TAPI only defines LayerProtocol as extensible (isLeaf=false)
    - the rest of updates includes changes due to Uml2Yang name-conversion rule
    update - mainly prepending and appending &#39;-&#39; to numbers in a name, e.g. P2P-&gt;
    p-2-p

* __Tagged all enumerations as leaf to prevent generation of yang identity__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 24 May 2017 13:35:06 -0400
    [39dbdc1b08ba695edae6f0da2c7350c31c2223a0](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/39dbdc1b08ba695edae6f0da2c7350c31c2223a0) 
    

* __Yang Validation Fix - removed readOnly for uuId &amp; localId__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Sun, 7 May 2017 15:11:29 -0400
    [ff9dc6b1422b92075a14b4c669525a9d05322b7d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ff9dc6b1422b92075a14b4c669525a9d05322b7d) 
    Apparently since these attributes are used as keys in configurable (RW) lists,
    this fails strict yang validation tests. The only other way to fix this is to
    have two separate copies of groupings for GlobalClass and LocalClass  - RO &amp; RW
    versions of these attributes to used in state and config trees respectively

* __Updates to Yang files generated using latest Eagle Xmi2Yang tool__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 2 May 2017 14:46:36 -0400
    [c4987b2efea3cf5b532be143eae7fbb1c0e2e15b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c4987b2efea3cf5b532be143eae7fbb1c0e2e15b) 
    - also includes consolidation of the Oam operations under a single interface
    class due to tool not recognizing an empty sub-interface that aggregates
    multiple non-empty super interfaces.

* __Mininet example network__

    [Ricard Vilalta](mailto:rvilalta@gmail.com) - Tue, 25 Apr 2017 13:22:38 +0100
    [8e383774b630edda910f46b5f74fc79758b98739](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/8e383774b630edda910f46b5f74fc79758b98739) 
    

* __Updated swagger files related to recent OAM and Notification updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 17 Apr 2017 12:43:08 -0400
    [7defcf098e6d2cd7a09c008d6ea9ebbe13071795](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7defcf098e6d2cd7a09c008d6ea9ebbe13071795) 
    - Using composition instead of specialization for Alarm/Tca info
    - Added an Connection reference to OAM Service

* __Updated Yang/Tree files related to recent OAM and Notification updates__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 17 Apr 2017 12:41:28 -0400
    [f74f17f6236e0e4bc722da6c4bb03b5a93b50012](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/f74f17f6236e0e4bc722da6c4bb03b5a93b50012) 
    - Using composition instead of specialization for Alarm/Tca info
    - Added an Connection reference to OAM Service

* __Added an Connection reference to OAM Service__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 17 Apr 2017 12:26:46 -0400
    [46d99be780d47b7d57df275273fed02906cc921c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/46d99be780d47b7d57df275273fed02906cc921c) 
    These updates are result of the 3-hour 04/13 IMP discussion

* __Bug Fix: Removed StrictComposite for PathHasLink association__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Sun, 16 Apr 2017 12:01:15 -0400
    [7fea1cb372c3bbadd143583e185b35f09acda3b6](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7fea1cb372c3bbadd143583e185b35f09acda3b6) 
    

* __Using composition instead of specialization for Alarm/Tca info__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 13 Apr 2017 16:01:39 -0400
    [325bfcedd6b80977ba4f689c9a5a063b6dcbaafd](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/325bfcedd6b80977ba4f689c9a5a063b6dcbaafd) 
    The use of inheritance/specialization to extend base Notification class will
    require the Yang mapping tool to create explicit lists for each of the concrete
    sub-classes as well as the super-class. Conditionally composing the
    Notification class is a better pattern if it is prefered to have single list
    for all types of Notifications.

* __Generated Tree and Swagger files for latest TAPI Yang__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 5 Apr 2017 17:46:34 -0400
    [0a14a863d59ee14e181aae408289e7cddc3d57c7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/0a14a863d59ee14e181aae408289e7cddc3d57c7) 
    

* __Bug Fix: Manually fixed RPC parameter of complex data-type mapping__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 5 Apr 2017 17:45:37 -0400
    [83a5a87e1829ab2c361aab19777872977a434457](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/83a5a87e1829ab2c361aab19777872977a434457) 
    The tool is unable to resolve the class/grouping for complex types when used in
    rpc-parameters. May have to do something with renaming grouping with -g suffix

* __Miscellaneous fixes overlooked in the initial cut (key, readonly, etc)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 5 Apr 2017 16:46:35 -0400
    [b1f91b13720a802c1867b1f6e0ba2dadea2de9d5](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b1f91b13720a802c1867b1f6e0ba2dadea2de9d5) 
    

* __Initial commit of the Node Constraint model__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 4 Apr 2017 17:53:37 -0400
    [1fc6a20150f24773eeca42b0e7543687f5464575](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/1fc6a20150f24773eeca42b0e7543687f5464575) 
    

* __Minor fixes in the ODU Specify association target__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 3 Apr 2017 14:51:47 -0400
    [6f879af8167394e66323d7800e8527fdb9dd550a](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/6f879af8167394e66323d7800e8527fdb9dd550a) 
    

* __Yang files generated after OpenModelProfile/OpenInterfaceModelProfile__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 3 Apr 2017 14:37:37 -0400
    [4e9699e6d60f69600634e821c60ba7bc258ef9bc](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4e9699e6d60f69600634e821c60ba7bc258ef9bc) 
    - Generated Yang files after application of newly dis-aggregated 
    OpenModelProfile/OpenInterfaceModelProfile to TAPI
    - Rename of all groupings with -g suffix
    - Application of &lt;Specify&gt; stereotype for augmentation
    - Uses latest version Uml2Yang eagle tool 

* __Minor fixes and added description to Specify association__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 3 Apr 2017 12:45:58 -0400
    [b28e5d701d1f3c32ada3dafd52c0552529280766](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b28e5d701d1f3c32ada3dafd52c0552529280766) 
    

* __Migration of InterfaceModelProfile to OpenInterfaceModelProfile__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 3 Apr 2017 09:02:00 -0400
    [95a1f26f829b299fbaa9f6ba4e1be59459d32a60](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/95a1f26f829b299fbaa9f6ba4e1be59459d32a60) 
    

* __Added an empty prefix for the tool to work__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 3 Apr 2017 08:46:46 -0400
    [eb0d1426cc0bb53a9be19644875ccf002006aca5](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/eb0d1426cc0bb53a9be19644875ccf002006aca5) 
    

* __Snapshot based on agreement in TAPI call on 03-28-2017__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 31 Mar 2017 17:20:53 -0400
    [eac6efc169892fb5c29422ec2f6d4ac1f7b78b66](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/eac6efc169892fb5c29422ec2f6d4ac1f7b78b66) 
    

* __Running TAPI_RI on top of ONOS server__

    [Ricard Vilalta](mailto:rvilalta@gmail.com) - Tue, 28 Mar 2017 14:33:10 +0100
    [7cf4dddd4e26ee57cb9f3af75e4b95f1603b5141](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7cf4dddd4e26ee57cb9f3af75e4b95f1603b5141) 
    

* __Resolve Merge conflict__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 27 Mar 2017 20:18:22 -0400
    [aa476c09301536c38132eb7646f4d04a773befc4](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/aa476c09301536c38132eb7646f4d04a773befc4) 
    

* __cleanup - removed old, auto-generated UML figures for yang model__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 27 Mar 2017 20:13:59 -0400
    [00be6c56a6e246f03094b13f551179b0678ffa50](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/00be6c56a6e246f03094b13f551179b0678ffa50) 
    

* __TAPI migration to new OpenModelProfile + InterfaceModelProfile__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 27 Mar 2017 20:13:13 -0400
    [e5231846695f75c494d173f73f3e8a571ae7ded3](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e5231846695f75c494d173f73f3e8a571ae7ded3) 
    

* __Rename sep &amp; serviceEndPoint to endPoint__

    [Donald Hunter](mailto:donaldh@cisco.com) - Tue, 21 Mar 2017 15:53:52 +0000
    [3655b557f46f4db6e9762494d891610ad93400fc](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/3655b557f46f4db6e9762494d891610ad93400fc) 
    

* __Change sep to serviceEndPoint__

    [Donald Hunter](mailto:donaldh@cisco.com) - Mon, 20 Mar 2017 15:04:25 +0000
    [d075de9e37478901b32edda45a8a1f68a2bc1beb](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/d075de9e37478901b32edda45a8a1f68a2bc1beb) 
    This makes input param in ConnectivityService.createConnectivityService 
    consistent with the field name in the model and return value.
    

* __Initial ONOS mapping files__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Mar 2017 22:46:16 -0500
    [fb9508093dbd04c4849b7befd9858624b7500bd2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fb9508093dbd04c4849b7befd9858624b7500bd2) 
    

* __Initial ODL mapping files__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Mar 2017 22:45:57 -0500
    [647e279068862b3e405f03fd66f714f6cc8f5ca1](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/647e279068862b3e405f03fd66f714f6cc8f5ca1) 
    

* __Eclipse setting files for TAPI RI__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Mar 2017 22:45:36 -0500
    [4364297cb750b6d83b3de2c9afc5e70540687544](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4364297cb750b6d83b3de2c9afc5e70540687544) 
    

* __TAPI RI Project files using PyDev plugin__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Mar 2017 22:25:38 -0500
    [c3b874905396c27ef61f3689a166858587aadba9](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c3b874905396c27ef61f3689a166858587aadba9) 
    

* __Deleted the maven project file as it is not needed__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 7 Mar 2017 15:43:46 -0500
    [b1a257cb5badb3a8d01255efdb6f75ec8f232d67](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b1a257cb5badb3a8d01255efdb6f75ec8f232d67) 
    

* __Adding TapiApp for RI__

    [Ricard Vilalta](mailto:rvilalta@gmail.com) - Mon, 6 Mar 2017 13:57:25 +0000
    [f82a31d20cc8e1e1d2840598190a19f2a70bcb3b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/f82a31d20cc8e1e1d2840598190a19f2a70bcb3b) 
    

* __Changes due to using the latest version of yang2swagger tool__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:37:45 -0500
    [a07d239d6c3fb83c209ef1929ae7d88b522c6563](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a07d239d6c3fb83c209ef1929ae7d88b522c6563) 
    

* __Yang/Swagger generation after Alarm/TCA feature addition__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:36:58 -0500
    [e7b5ad0f3425a32c65ce2c1dd12b74b2da3cf367](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e7b5ad0f3425a32c65ce2c1dd12b74b2da3cf367) 
    

* __Minor fix due to manual insertion of presence statement__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:36:20 -0500
    [507d7e672d9aaa38e45b9f905f2481ca8f885385](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/507d7e672d9aaa38e45b9f905f2481ca8f885385) 
    

* __Updates due to rename of ServiceEndPoint to ServiceInterfacePoint__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:34:56 -0500
    [390e00d85f8e82ee1c90c45644e75c33afc1d1d3](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/390e00d85f8e82ee1c90c45644e75c33afc1d1d3) 
    

* __Updates due to removal of TeLink. Path is now defined in terms of TeLink__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:33:51 -0500
    [7f1ad90028a9e8e4769988488df0dc928e7a0460](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7f1ad90028a9e8e4769988488df0dc928e7a0460) 
    

* __Removed TeLink class and use Link where TeLink was previously used__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:31:30 -0500
    [b17474c62571e106f76c6aaac482c2e5a3e740d7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b17474c62571e106f76c6aaac482c2e5a3e740d7) 
    Also updated LayerProtocolTransitionPac

* __Renamed ConnectivityServicePort to ConnectivityServiceEndPoint__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 14:29:19 -0500
    [3973449dda24b99195de3ef66ab259b6d31bf277](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/3973449dda24b99195de3ef66ab259b6d31bf277) 
    Also split the ConnectivityConstraint class into ConnectivityConstraint and
    TopologyConstraint classes Updated Create and Update RPC operations with
    missing parameters

* __Renamed ServiceEndPoint to ServiceInterfacePoint__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 1 Mar 2017 13:46:47 -0500
    [c59e0c4b9af2369997330feba390e84d61378287](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c59e0c4b9af2369997330feba390e84d61378287) 
    Also marked the GlobalClass::uuid and LocalClass::localId attributes as 
    read-only

* __Minor fixes to the usage associations in UML diagrams__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 22 Feb 2017 16:58:08 -0500
    [0890ac7cc40c1ab777b1acc8f88d42cc1e0a60ac](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/0890ac7cc40c1ab777b1acc8f88d42cc1e0a60ac) 
    

* __Updates from the Heidelberg interim meeting__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 14 Feb 2017 15:18:53 -0500
    [2f1e8d6e680cf05b6a5de4d71faca429fad35865](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/2f1e8d6e680cf05b6a5de4d71faca429fad35865) 
    

* __Minor typo fix__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 14 Feb 2017 13:05:18 -0500
    [ebf5fcc79269d26095369ac43a6e7ddef8aa70a3](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/ebf5fcc79269d26095369ac43a6e7ddef8aa70a3) 
    

* __Updates to TAPI Protection model after the Heidelberg Interim meeting__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 14 Feb 2017 13:00:15 -0500
    [fb45d9daa24be5f2125a88ec56c1de0d2e0e9e6a](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/fb45d9daa24be5f2125a88ec56c1de0d2e0e9e6a) 
    

* __Initial TAPI OAM Model__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 6 Feb 2017 05:54:51 -0500
    [0e729eb07d7e24ae141402d0d2eda2b1332ffcce](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/0e729eb07d7e24ae141402d0d2eda2b1332ffcce) 
    

* __Initial draft of resilience/protection/switch model__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Sat, 4 Feb 2017 16:31:42 -0500
    [c3d060a8379a1091a860ab519d989ec3b9e37bce](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c3d060a8379a1091a860ab519d989ec3b9e37bce) 
    

* __Added ServiceAffecting property to the Alarm Notification__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Mon, 30 Jan 2017 10:50:14 -0500
    [a8ad56a583c44b6789d0ad7a6551b25b9bc040c7](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a8ad56a583c44b6789d0ad7a6551b25b9bc040c7) 
    

* __Draft Alarm/TCA Model__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 26 Jan 2017 13:05:24 -0500
    [4a1032a8f8f3988765e6653bae5b14e8afddd359](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4a1032a8f8f3988765e6653bae5b14e8afddd359) 
    

* __Cleanup YANG dir: Removed tree/ img/ pyan_uml/ sub-folder &amp; files__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 12 Jan 2017 13:40:11 -0500
    [cd34c0745cb726294370964be3cba88ac877c0ab](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/cd34c0745cb726294370964be3cba88ac877c0ab) 
    - Following common yang practices, the pyang-generated .tree are in the YANG
    directory next to the .yang files.

* __tree files after the context attributes read-only property fix__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 11 Jan 2017 18:22:20 -0500
    [40a89b086f90e6f2b3a4675fa04324a06f0b3b41](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/40a89b086f90e6f2b3a4675fa04324a06f0b3b41) 
    

* __Fixed read-only property of the Context&#39;s resource &amp; service attributes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 11 Jan 2017 17:46:06 -0500
    [cdf4f17dc96c63d108baf419119ca15fb62e5e52](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/cdf4f17dc96c63d108baf419119ca15fb62e5e52) 
    During the split-up of TapiCommon:Context into individual module-specific
    contexts, the read-only property for the context&#39;s attributes that were moved
    to the module-specific contexts were not correctly set. 

* __Updated after fixes in EAGLE tooling__

    [Ricard Vilalta](mailto:ricard.vilalta@cttc.es) - Wed, 11 Jan 2017 05:08:42 -0800
    [a7141e00dc64381370ddc67f87f8a3f3677d83ff](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/a7141e00dc64381370ddc67f87f8a3f3677d83ff) 
    

* __Cleaning old files__

    [Ricard Vilalta](mailto:ricard.vilalta@cttc.es) - Mon, 9 Jan 2017 06:01:20 -0800
    [7e45debfd8dedc61abf7e4ceac3bea1fb3b3222f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7e45debfd8dedc61abf7e4ceac3bea1fb3b3222f) 
    

* __Cleaning old files__

    [Ricard Vilalta](mailto:ricard.vilalta@cttc.es) - Mon, 9 Jan 2017 05:59:52 -0800
    [032ca5a7bae47c16622013e74fe5d73bfbc37c3f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/032ca5a7bae47c16622013e74fe5d73bfbc37c3f) 
    

* __Renaming and updating of pyang results__

    [Ricard Vilalta](mailto:ricard.vilalta@cttc.es) - Mon, 9 Jan 2017 05:54:56 -0800
    [1c49e351dacf8036ef5c51cdf13807a4c4eee83d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/1c49e351dacf8036ef5c51cdf13807a4c4eee83d) 
    

* __Fix #157: Deleted ExtensionsSpec class and _extensions attribute__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 4 Jan 2017 17:28:52 -0500
    [7c4f80784ba63c4a9006c7918ec043ee769806a9](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/7c4f80784ba63c4a9006c7918ec043ee769806a9) 
    - Deleted the _extensions attribute from the GlobalClass and LocalClass as it
    is not being used. Using the spec-model, it is possible to specify extensions
    to any attribute of a class by annotating with the
    &lt;SpecTarget&gt; stereotype. Hence a special attribute is unnecessary

* __Fix #157: Changed UML to augment Context rather than its attributes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 4 Jan 2017 16:44:38 -0500
    [283deeb9937147ead81a3fad25935e68de54bb4d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/283deeb9937147ead81a3fad25935e68de54bb4d) 
    

* __Fix #157: Changed UML to augment Context rather than its attributes__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 4 Jan 2017 16:42:29 -0500
    [b9b8f4346c353a58d90fcaf756b94020e04d48b2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b9b8f4346c353a58d90fcaf756b94020e04d48b2) 
    Updated the UML model with following changes to simplify the TAPI specification
    model:
    - Rather than define generic attributes in TAPI Context
    (_serviceEndPoint, _topology, _connection, _path, _notification, etc) and then
    augment those attributes in the specific TAPI modules, fixed model to define an
    almost empty TAPI context (only contains
    _serviceEndPoint attribute) in the TapiCommon module and then augmenting this
    base Context in the specific TAPI modules to specify additional relevant
    attributes.
    - Also updated the technology-specific augmentation to specify/extend the
    layerProtocol itself rather than the extensions attribute of layerProtocol.
    This eliminates an additional level of indirection.

* __Partial fix #157: manual-fixed yang files for pyang/swagger compilation__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 4 Jan 2017 13:11:50 -0500
    [2e8c4a34b844f415dc267b729e4e81c27e3d7b21](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/2e8c4a34b844f415dc267b729e4e81c27e3d7b21) 
    

* __Fix #179, #180 - manual-fixed yang files for pyang/swagger compilation__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 30 Dec 2016 09:27:48 -0500
    [f9289f14e9d56fe6165be9cc25ccdfd724424ff8](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/f9289f14e9d56fe6165be9cc25ccdfd724424ff8) 
    

* __Minor UML Model fixes for proper YANG generation__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 22 Dec 2016 11:22:44 -0500
    [c5f41a76d6651dcc50ba160abd653ee889fc4a9f](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c5f41a76d6651dcc50ba160abd653ee889fc4a9f) 
    

* __prefix statement fix using the eagle xmi2yang tool update b96e2a5__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 21 Dec 2016 13:38:20 -0500
    [b98720c7865e0aea2001fdeb6a88a7a30c55f49d](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/b98720c7865e0aea2001fdeb6a88a7a30c55f49d) 
    

* __TAPI Multi-layer examples presented at the ONF 2016 Fall MWD__

    [Karthik Sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 21 Dec 2016 08:19:17 -0500
    [c5807944bb1333a8ed83d6beea3e55922d006495](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c5807944bb1333a8ed83d6beea3e55922d006495) 
    

* __Generated TAPI Yang files after patching the xmi2yang tool__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 16 Dec 2016 16:39:29 -0500
    [5183e4190c4a0d486527ddbabf7e201e11de7e15](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5183e4190c4a0d486527ddbabf7e201e11de7e15) 
    - Fixed to NOT generate top-level containers/lists for all concrete classes,
    but just for TAPI Context
    - Removed code that prevented generation of attributes annotated with
    &#34;DefinedBySpec&#34; stereotype

* __Updated UML files to rename spec-targets as per new yang renaming__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Fri, 16 Dec 2016 16:35:01 -0500
    [0ca78c6185b9c1bd4704400b14e8012919562eac](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/0ca78c6185b9c1bd4704400b14e8012919562eac) 
    

* __Raw TAPI YANG files generated by the EAGLE xmi2yang tool (e95c9fb)__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Thu, 15 Dec 2016 14:02:39 -0500
    [5c6f2dfea21417e918839fe668a47c568a0d9b8c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/5c6f2dfea21417e918839fe668a47c568a0d9b8c) 
    

* __Renamed TAPI Yang files to follow Yang naming conventions__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 14 Dec 2016 17:00:25 -0500
    [4cfbff0baec7831c8013f7f9a846546a7e601651](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4cfbff0baec7831c8013f7f9a846546a7e601651) 
    No other changes are made to the file content. This is to ensure that the
    current code is base-lined under new file names and will be followed by changes
    to content to fix module names, etc 

* __Renamed papyrus models Tapi &amp; TapiModel to TapiCommon &amp; TapiOverview__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Wed, 14 Dec 2016 16:50:52 -0500
    [95e3037b73a16fc0567607100423f3661e8ec9e8](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/95e3037b73a16fc0567607100423f3661e8ec9e8) 
    

* __UML Cleanup: CoreModel and Tapi skeleton diagrams__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 20:10:55 -0500
    [66ea8ef7248b821da84b535d07356dd2d4d22cbc](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/66ea8ef7248b821da84b535d07356dd2d4d22cbc) 
    

* __Added XOR rule for Topology containment__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 19:54:32 -0500
    [9bd74eaad4ecd1cd49cebc678d8d81f3e951720a](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/9bd74eaad4ecd1cd49cebc678d8d81f3e951720a) 
    

* __Fixes #168: Minor association label fix__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 18:03:10 -0500
    [c4d680222bd186a0493b8e8bcfc622356b20981c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c4d680222bd186a0493b8e8bcfc622356b20981c) 
    

* __Fixes #130, #141, #159__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 17:39:41 -0500
    [e778d228cda132f5e2580d46ae0daa84e2aec0b8](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/e778d228cda132f5e2580d46ae0daa84e2aec0b8) 
    - #130: Renamed the attribute ServicePort.servicelayer to 
    ServicePort.layerProtocolName
    - #130: Renamed the attribute ConnectivityConstraint.serviceLayer to 
    ConnectivityConstraint.preferredTransportLayer
    - #141: Renamed existing attributes ConnectivityConstraint._includePath and
    ConnectivityConstraint._excludePath to ConnectivityConstraint._includeRoute and 
    ConnectivityConstraint._exludeRoute
    - #141: Added new attributes ConnectivityConstraint._includePath and 
    ConnectivityConstraint._exlcludePath that refer to an existing Path in the TAPI
    provider, that was previously created via PathComputation API
    - #159: Added the attribute ConnectivityConstraint._corouteInclusion that
    optionally refers to an existing ConnectivityService for co-routing
    

* __Fixes #168: Merged ConnectionPort into ConnectionEndPoint__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 15:01:43 -0500
    [21f8e1a5f5cd741f55087f2890c449170f366ce6](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/21f8e1a5f5cd741f55087f2890c449170f366ce6) 
    Also renamed following attributes
    - ConnectionEndPoint.direction to ConnectionEndPoint.terminationDirection
    - ConnectionPort.direction to ConnectionEndPoint.connectionPortDirection
    - ConnectionPort.role to ConnectionEndPoint.connectionPortRole

* __Fixes #167: Merged LinkPort into NodeEdgePoint__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 14:23:15 -0500
    [c8d49fc77d203e80a0e19dd39bc781afd213d3a2](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/c8d49fc77d203e80a0e19dd39bc781afd213d3a2) 
    Also renamed following attributes
    - NodeEdgePoint.direction to NodeEdgePoint.terminationDirection
    - LinkPort.direction to NodeEdgePoint.linkPortDirection
    - LinkPort.role to NodeEdgePoint.linkPortRole

* __UML CoreIM-TAPI PruneAndRefactor Realization-Associations cleanup/delete__

    [karthik-sethuraman](mailto:karthik.sethuraman@necam.com) - Tue, 13 Dec 2016 13:41:11 -0500
    [4d630d2b2788cdb33fe048bc55ef18c1b5147a71](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/4d630d2b2788cdb33fe048bc55ef18c1b5147a71) 
    This needs to be recreated in TAPI 2.0 as these were broken during CoreIM 1.2
    import

* __Delete .txt__

    [Ricard Vilalta](mailto:rvilalta@gmail.com) - Tue, 22 Nov 2016 11:17:22 +0100
    [665bb6f6aa0bbe03269dca75a0c7dc5fdf07477b](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/665bb6f6aa0bbe03269dca75a0c7dc5fdf07477b) 
    

* __Adding TAPI_RI Tester__

    [Ricard Vilalta](mailto:ricard.vilalta@cttc.es) - Tue, 22 Nov 2016 02:16:29 -0800
    [0b394f70590bf49da440eeff7f4b70fe63f3465c](https://github.com/OpenNetworkingFoundation/Snowmass-ONFOpenTransport/commit/0b394f70590bf49da440eeff7f4b70fe63f3465c) 
    


