object mergeSortedArrays {
  def main(args:Array[String]): Unit = {
    def mergeArrays(arr1: Array[Double],arr2: Array[Double],
                    n1:Int,n2:Int): List[Double] = {
      var i:Int = 0
      var j:Int = 0
      var arr3: Array[Double] = Array()
      while (i < n1) {
        arr3 = arr3 :+ arr1(i)
        i += 1
      }
      while(j < n2){   
        arr3 = arr3 :+ arr2(j) 
        j += 1
      }
      arr3.sortWith(_ < _).toList
  }
  val arr1 = Array(1, 2, 3, 5, 7, 23, 50, 1000, 1000.564)
  val n1 = arr1.length
  println (n1)

  val arr2 = Array(2, 4, 6, 8, 10,-34,-1000,-3.4565)
  val n2 = arr2.length
  println (n2)

  val result = mergeArrays(arr1,arr2,n1,n2)
  println(s"Array after merging is $result")
  }
}