using System;

namespace MOOPLab2
{
    public class SortUtils
    {
        static void Main(string[] args)
        {
            var me = ShellSort(new int[] { 1, 2, 11, 4, 2, 3, 56, 1, 0 });
            foreach (int i in me) {
                Console.WriteLine(i);
            }
        }
        static public int[] ShellSort(int[] array)
        {
            var d = array.Length / 2;
            while (d >= 1)
            {
                for (var i = d; i < array.Length; i++)
                {
                    var j = i;
                    while ((j >= d) && (array[j - d] > array[j]))
                    {
                        var t = array[j];
                        array[j] = array[j - d];
                        array[j - d] = t;
                        j = j - d;
                    }
                }

                d = d / 2;
            }

            return array;
        }
    }
}