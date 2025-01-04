import { app, api, ComfyWidgets, LiteGraph, TLGraphNode } from './libs/index.js';
import { commonPrefix, displayContext } from './libs/common.js';
app.registerExtension({
    name: 'bongsang.utils.any_info',
    beforeRegisterNodeDef(nodeType, nodeData, appFromArg) {
        if (nodeData.name === 'AnyInfo') {
            displayContext(nodeType, appFromArg, 3);
        }
    },
});
