<template>
    <div>
        <el-container>
            <el-header class="custom-header">This is a webpage that updates information recruitment of tech company every day.</el-header>
            <el-main>Authorized by James Huang</el-main>
        </el-container>
        <div class="layout-container">
            <div class="left">
                <el-row class="tac">
                    <el-col :span="24">
                        <h1>Navigation Bar</h1>
                        <el-menu
                            default-active="2"
                            class="el-menu-vertical-demo">
                        <el-menu-item @click="selectContent(1)">
                            <i class="el-icon-menu"></i>
                            <span slot="title">Frontend Engineer</span>
                        </el-menu-item>
                        <el-menu-item @click="selectContent(2)">
                            <i class="el-icon-menu"></i>
                            <span slot="title">Backend Engineer</span>
                        </el-menu-item>
                        <el-menu-item @click="selectContent(3)">
                            <i class="el-icon-menu"></i>
                            <span slot="title">Search by yourself...</span>
                        </el-menu-item>
                        </el-menu>
                    </el-col>
                </el-row>
            </div>

            <div class="right">
                <div v-if="currentSelection === 1">
                    <el-button @click="crawlData" size="large" type="primary" text-align="center">Refresh</el-button>
                    <h5>If you want to refresh data, click refresh button and refresh the webpage!</h5>
                    <br>
                    <el-table :data="tableData1" stripe style="width: 100%">
                    <el-table-column prop="title" label="title" width="180"></el-table-column>
                    <el-table-column prop="company" label="company" width="180"></el-table-column>
                    <el-table-column prop="location" label="location"></el-table-column>
                    <el-table-column prop="url" label="superlink">
                        <template slot-scope="scope">
                            <el-link :href="scope.row.url" target="_blank">{{ "Go to this job" }}</el-link>
                        </template>
                    </el-table-column>
                    </el-table>
                </div>

                <div v-if="currentSelection === 2">
                    <el-button @click="crawlData" size="large" type="primary" text-align="center">Refresh</el-button>
                    <h5>If you want to refresh data, click refresh button and refresh the webpage!</h5>
                    <br>
                    <el-table :data="tableData2" stripe style="width: 100%">
                    <el-table-column prop="title" label="title" width="180"></el-table-column>
                    <el-table-column prop="company" label="company" width="180"></el-table-column>
                    <el-table-column prop="location" label="location"></el-table-column>
                    <el-table-column prop="url" label="superlink">
                        <template slot-scope="scope">
                            <el-link :href="scope.row.url" target="_blank">{{ "Go to this job" }}</el-link>
                        </template>
                    </el-table-column>
                    </el-table>
                </div>

                <div v-if="currentSelection === 3">
                    <el-container>
                    <el-header class="custom-header">Search by yourself</el-header>
                    </el-container>
                    <el-input
                        placeholder="Please input the job title you want to search"
                        v-model="input"
                        clearable>
                    </el-input>
                    <div>
                        <el-button @click="crawlData" size="large" type="primary" text-align="center">Search</el-button>
                    </div>
                </div>
            </div>
        </div>
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
                tableData2: ddata2,
                currentSelection: 1,
                input: '',
            };
        },

        methods: {
            selectContent(selection) {
                this.currentSelection = selection;
            },

            crawlData() {
                console.log("crawlData method triggered on myPage.vue!");
                // Make a POST request to the backend API endpoint
                fetch('http://localhost:8081/crawl', { method: 'POST' })
                // .then((response) => response.json())
                // .then((data) => {
                //     // Handle the crawled data here, e.g., update the Vue component's data
                //     console.log(data);
                // })
                .catch((error) => {
                    console.error('Failed to crawl data:', error);
                });
            },
        },
    };
</script>

<style>
    .layout-container {
    display: flex; /* Use flex display to arrange items horizontally */
    }

    body {
      margin: 0;
      padding: 0;
      display: flex;
    }

    .left {
      flex: 1;
      background-color: lightgray;
      padding: 20px;
    }
    
    .right {
      flex: 3;
      background-color: lightblue;
      padding: 20px;
    }

    .custom-header {
        font-size: 40px; /* Set your desired font size */
    }

    .el-button {
        size: "large";
        text-align: center
    }

    .el-row {
        margin-bottom: 20px;
        &:last-child {
            margin-bottom: 0;
        }
    }
    .el-col {
        border-radius: 4px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #d3dce6;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
    
    .el-header{
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    
    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: left;
        line-height: 10px;
    }
    
    body > .el-container {
        margin-bottom: 40px;
    }
</style>