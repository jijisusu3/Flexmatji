<template>
  <form @submit.prevent="onSubmit">
    <table style="padding-top:50px" align=center width=900 border=0 cellpadding=2 >
      <tr>
      <td height=50 align= center bgcolor=#ccc><font style="font-size:20px;" color=black> 글쓰기</font></td>
      </tr>
      <tr>
      <td bgcolor=white>
      <table class = "table2">
        <tr>
        <div class="my-4">
          <td>커뮤니티: </td>
          <td><select v-model="newArticle.community_id" name="id" id="community_id">
            <option value="">--게시판 선택--</option>
            <option value="1" disabled>공지사항</option>
            <option value="2">자유게시판</option>
            <option value="3">영화 리뷰</option>
            <option value="4">공포</option>
            <option value="5">MARVEL</option>
            <option value="6">애니메이션</option>
            <option value="7">SF</option>
          </select></td>
        </div>
        </tr>
        <tr>
        <div>
          <td><label for="title">title: </label></td>
          <td><input v-model="newArticle.title" type="text" id="title"></td>
        </div>
        </tr>
        <tr>
        <div>
          <td><label for="content">contnet: </label></td>
          <td><textarea cols=85 rows=15 v-model="newArticle.content" type="text" id="content"></textarea></td>
        </div>
        </tr>
      </table>

        <center>
          <button class="btn btn-secondary">{{ action }}</button>
        </center>
      </td>
      </tr>
  </table>
<!-- 

    <div>
      <label for="content">contnet: </label>
      <textarea v-model="newArticle.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div> -->
  </form>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          community_id: this.article.community_id,
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.id,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style scoped>

  table.table2{
    border-collapse: separate;
    border-spacing: 1px;
    text-align: left;
    line-height: 1.5;
    border-top: 1px solid #ccc;
    margin : 20px 10px;
  }
  table.table2 tr {
    width: 50px;
    padding: 10px;
    font-weight: bold;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
  }
  table.table2 td {
    width: 100px;
    padding: 10px;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
  }
 

</style>
