<template>
    <div style="background-color: #606266;">
        <el-button @click="changeData" size="large" type="primary" text-align="center">Refresh</el-button>
        <h5>If you want to refresh data, click refresh button and refresh the webpage!</h5>
        <el-table :data="tableData1" stripe style="width: 100%">
        <el-table-column prop="title" label="title" width="180"></el-table-column>
        <el-table-column prop="company" label="company" width="180"></el-table-column>
        <el-table-column prop="location" label="location"></el-table-column>
        <el-table-column label="url">
            <template slot-scope="scope">
            <el-link :href="scope.row.url" target="_blank">{{ "Go" }}</el-link>
            </template>
        </el-table-column>
        </el-table>

    </div>
</template>

<script>
    import frontendData from '../../data/frontendengineer.json';
    // import backendData from '../../data/backendengineer.json';

    var ddata1 = []

    for (var key in frontendData) {
        ddata1.push(frontendData[key]);
    }

    export default {
        data() {
            return {
                tableData1: ddata1,
                // tableData2: ddata2
            };
        },
        
        methods: {
            update() {
                const updated = require('../../data/frontendengineer.json');
                this.tableData1 = [];  // Clear the existing data
                for (var key in updated) {
                    this.tableData1.push(updated[key]);
                }
            }
        }
    };
</script>
