<template>
    <div>
        <el-container>
        <el-header class="custom-header">This is a webpage that updates information recruitment of of tech company every day.</el-header>
        <el-main>Authorized by James Huang</el-main>
        </el-container>
        <br>
        <div>
            <!-- <el-input placeholder="Please type the job you want to search" v-model="input" clearable></el-input> -->
            <el-button @click="crawlData" size="large" type="primary" text-align="center">Refresh</el-button>
        </div>
        <br>

        <el-container>
        <el-header class="custom-header">Machine Learning Engineer</el-header>
        <el-main>
            <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="title" label="title" width="180"></el-table-column>
            <el-table-column prop="company" label="company" width="180"></el-table-column>
        </el-table>
        </el-main>
        </el-container>
        
        <el-container>
        <el-header class="custom-header">Backend Engineer</el-header>
        <el-main>
            <!-- <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="title" label="title" width="180"></el-table-column>
            <el-table-column prop="company" label="company" width="180"></el-table-column>
            </el-table> -->

        </el-main>
        </el-container>
        
    </div>
  </template>

  
<script>
// window.alert("asdf");

export default {
    data() {
        return {
            tableData: [
                {
                title: '',
                company: '',
                },
                {
                title: '',
                company: '',
                },
                {
                title: '',
                company: '',
                },
                {
                title: '',
                company: '',
                },
            ],
            input: '', 
        };
    },

    methods: {
        crawlData() {
            // window.alert("crawlData method triggered!");
            console.log("crawlData method triggered on myPage.vue!");
            // Make a POST request to the backend API endpoint
            fetch('http://localhost:8080/crawl', { method: 'POST' })
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
  