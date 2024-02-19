using NUnit.Framework;
using System;
using MOOPLab2;

namespace MOOPLab2Test
{
    [TestFixture]
    internal class SortUtilsTest
    {
        static void Main(string[] args)
        {
            
        }
        // Тестирование метода ShellSort
        [Test()]
        public void ShellSortTestNormalArrayWithUniqueElements()
        {
            //Класс эквивалентности 1
            int[] a = { 1, 2, 9, -4, 5 };
            int[] expected = {-4, 1, 2, 5, 9 };
            int[] actual;
            actual = SortUtils.ShellSort(a);
            Assert.That(actual, Is.EquivalentTo(expected));
        }
        [Test()]
        public void ShellSortTestNormalArrayWithSameElements()
        {
            //Класс эквивалентности 2
            int[] a = { 2, 2, 2 };
            int[] expected = { 2, 2, 2 };
            int[] actual;
            actual = SortUtils.ShellSort(a);
            Assert.That(actual, Is.EquivalentTo(expected));
        }
        [Test()]
        public void ShellSortTestNormalArrayWithRepeatedElements()
        {
            //Класс эквивалентности 3
            int[] a = { 1, 2, 2, 2, 1, 4 };
            int[] expected = {1, 1, 2, 2, 2, 4 };
            int[] actual;
            actual = SortUtils.ShellSort(a);
            Assert.That(actual, Is.EquivalentTo(expected));
        }
        [Test()]
        public void ShellSortTestArrayWithOneElement()
        {
            //Класс эквивалентности 4
            int[] a = { 3 };
            int[] expected = { 3 };
            int[] actual;
            actual = SortUtils.ShellSort(a);
            Assert.That(actual, Is.EquivalentTo(expected));
        }
        [Test()]
        public void ShellSortTestEmptyArray()
        {
            //Класс эквивалентности 5
            int[] a = { };
            int[] expected = { };
            int[] actual;
            actual = SortUtils.ShellSort(a);
            Assert.That(actual, Is.EquivalentTo(expected));
        }
        [Test()]
        public void ShellSortTestEmptyArrayExeption()
        {
            //Класс эквивалентности 6 (ошибочный)
            int[] a = null;
            int[] actual;
            Assert.Throws<NullReferenceException>(
            () => { actual = SortUtils.ShellSort(a); }
            );
        } 
    }

}