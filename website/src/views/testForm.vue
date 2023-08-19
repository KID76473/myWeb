<template>
    <div>
    <!-- <h1>table</h1> -->
    <el-table
    :data="tableData1"
    stripe
    style="width: 100%">
    <el-table-column
        prop="date"
        label="title"
        width="180">
    </el-table-column>
    <el-table-column
        prop="company"
        label="company"
        width="180">
    </el-table-column>
    <el-table-column
        prop="location"
        label="location">
    </el-table-column>
    <el-table-column
        prop="benefits"
        label="benefits">
    </el-table-column>
    <el-table-column
        prop="description"
        label="description">
    </el-table-column>
    </el-table>

    <el-table
    :data="tableData2"
    stripe
    style="width: 100%">
    <el-table-column
        prop="date"
        label="title"
        width="180">
    </el-table-column>
    <el-table-column
        prop="company"
        label="company"
        width="180">
    </el-table-column>
    <el-table-column
        prop="location"
        label="location">
    </el-table-column>
    <el-table-column
        prop="benefits"
        label="benefits">
    </el-table-column>
    <el-table-column
        prop="description"
        label="description">
    </el-table-column>
    </el-table>
</div>
</template>

<script>
    import frontendData from '../../../data/frontendengineer.json';
    import backendData from '../../../data/BackendEngineer.json';

    var ddata1 = []
    var ddata2 = []

    for (var key in frontendData) {
        ddata1.push(frontendData[key]);
    }
    for (key in backendData) {
        ddata2.push(backendData[key]);
    }
    
    export default {
        data() {
            return {
                tableData1: ddata1,
                tableData2: ddata2
            };
        },
        
    };
</script>
