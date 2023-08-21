<script>
import { ElButton, ElLink, ElTable, ElTableColumn } from 'element-plus';
import frontendData from '../../../data/frontendengineer.json'; // Import your initial data here

export default {
    components: {
        ElButton,
        ElLink,
        ElTable,
        ElTableColumn,
    },
    data() {
        return {
            tableData1: frontendData, // Initialize with the initial data
        };
    },
    methods: {
        changeData() {
            // Re-import the updated data from the file
            const updatedData = require('../../../data/frontendengineer.json');
            this.tableData1 = updatedData;
        },
    },
};
</script>