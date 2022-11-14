<template>
  <main>
    <div class="container">
      <div class="row mt-3">
        <div class="col">
          <div id="cy"></div>
        </div>
      </div>
      <div class="row pt-2">
        <div class="col">
          <button class="btn btn-primary" @click="api.collapseAll()"> CollapseAllNodes</button>
          <button class="btn btn-primary" @click="api.expandAll()"> ExpandAllNodes</button>
        </div>
        <div class="col">
         <!-- <button class="btn btn-secondary" @click="colaLayout.run()">ColaLayout</button> -->
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import cytoscape from 'cytoscape';
import expandCollapse from 'cytoscape-expand-collapse';
import undoRedo from 'cytoscape-undo-redo';
import panzoom from 'cytoscape-panzoom'
import "cytoscape-panzoom/cytoscape.js-panzoom.css"
import cola from 'cytoscape-cola';
cytoscape.use(cola);
panzoom(cytoscape) ;
expandCollapse(cytoscape);
undoRedo(cytoscape);
import graphs from "../dataset/graph.json"
import fancyStyle from "../styles/fancy.json";

export default {
  data() {
    return {
      maxLayoutDuration: 1500,
      layoutPadding: 50,
      cy: null,
      api: null,
      colaLayout: null
    }
  },
  methods: {
   
  },
  mounted() {

    var parsed_graph = JSON.parse(graphs);

    let cy = cytoscape({

      container: document.getElementById('cy'),

      elements: parsed_graph,

      style: fancyStyle,

      layout: {
        name: 'cola'
      }
    });
   

    console.log(cy)
    // { layoutBy: { name: 'cola' }}
    cy.expandCollapse({});
    this.api = cy.expandCollapse('get');
    // api.collapseAll();
    // api.expandAll()
    // api.collapsibleNodes().forEach(node => {
    //   api.collapse(node);
    // });
    var defaults = {
      zoomFactor: 0.05, // zoom factor per zoom tick
      zoomDelay: 45, // how many ms between zoom ticks
      minZoom: 0.1, // min zoom level
      maxZoom: 10, // max zoom level
      fitPadding: 50, // padding when fitting
      panSpeed: 10, // how many ms in between pan ticks
      panDistance: 10, // max pan distance per tick
      panDragAreaSize: 75, // the length of the pan drag box in which the vector for panning is calculated (bigger = finer control of pan speed and direction)
      panMinPercentSpeed: 0.25, // the slowest speed we can pan by (as a percent of panSpeed)
      panInactiveArea: 8, // radius of inactive area in pan drag box
      panIndicatorMinOpacity: 0.5, // min opacity of pan indicator (the draggable nib); scales from this to 1.0
      zoomOnly: false, // a minimal version of the ui only with zooming (useful on systems with bad mousewheel resolution)
      fitSelector: undefined, // selector of elements to fit
      animateOnFit: function(){ // whether to animate on fit
        return false;
      },
      fitAnimationDuration: 1000, // duration of animation on fit

      // icon class names
      sliderHandleIcon: 'fa fa-minus',
      zoomInIcon: 'fa fa-plus',
      zoomOutIcon: 'fa fa-minus',
      resetIcon: 'fa fa-expand'
    };
    cy.panzoom(defaults);
    
  }
}
</script>
<style>
#cy {
  outline: solid 1px;
  height: 90vh;
}

.cy-expand-collapse-meta-edge {
  /* display: none !important; */
  /* color: red !important; */
}
</style>
