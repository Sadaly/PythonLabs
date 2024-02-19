using System;
namespace SimpleAlgorithmsApp
{
    public class LinkedList: Queue<int>
    {
        Node<int> head { get; set; }
        Node<int> tail { get; set; }
        int count { get; set; }
        public void Enqueue(int data)
        {
            Node<int> node = new Node<int>(data);
            Node<int> tempNode = tail;
            tail = node;
            if (count == 0)
                head = tail;
            else
                tempNode.Next = tail;
            count++;
        }
        public int Dequeue()
        {
            if (count == 0)
                throw new InvalidOperationException();
            int output = head.Data;
            head = head.Next;
            count--;
            return output;
        }
        // получаем первый элемент
        public int First
        {
            get
            {
                if (IsEmpty)
                    throw new InvalidOperationException();
                return head.Data;
            }
        }
        // получаем последний элемент
        public int Last
        {
            get
            {
                if (IsEmpty)
                    throw new InvalidOperationException();
                return tail.Data;
            }
        }
        public int Count { get { return count; } }
        public bool IsEmpty { get { return count == 0; } }

        Node<int> Queue<int>.head => throw new NotImplementedException();

        Node<int> Queue<int>.tail => throw new NotImplementedException();

        int Queue<int>.count => throw new NotImplementedException();

        public void Clear()
        {
            head = null;
            tail = null;
            count = 0;
        }

        public bool Contains(int data)
        {
            Node<int> current = head;
            while (current != null)
            {
                if (current.Data.Equals(data))
                    return true;
                current = current.Next;
            }
            return false;
        }
    }
    public class Node<T>
    {
        public Node(T data)
        {
            Data = data;
        }
        public T Data { get; set; }
        public Node<T> Next { get; set; }
    }
    interface Queue<T>
    {
        Node<T> head { get; }
        Node<T> tail { get; }
        int count { get; }
        void Enqueue(T data);
        // удаление из очереди
        T Dequeue();
        // получаем первый элемент
        T First { get; }
        T Last { get; }
        int Count { get; }
        bool IsEmpty { get; }
        void Clear();
        bool Contains(T data);
    }
}